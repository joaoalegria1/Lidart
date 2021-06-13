#!/usr/bin/env python3
# -*- coding: utf-8 -*-
################
#alteraçoes nas linhas 195, 196
################

from numpy import arange
import rospy
from std_msgs.msg import Int8
from std_msgs.msg import String, Float32MultiArray
import time

# Imports para o espelho e para o laser
import serial
from cust_MR_FPGA.cust_boards import Scuti
import cust_MR_FPGA.cust_commands as commands


photoReady1=0
photoReady2=0
FOVhor=0
FOVvert=0
stephor=0
stepvert=0
start=0
init=0
flag=0
stop=0
ready=0

ser1 = 0
Scuti1 = 0

## Laser function() 
def initializeLaser():

	global ser1

	start_laser = time.time()

	ser1 = serial.Serial()
	#ser1.port = "/dev/ttyUSB0"
	ser1.port = "/dev/ttyACM0"
	#ser.port = "/dev/ttyS2"	
	ser1.baudrate = 9600
	ser1.bytesize = serial.EIGHTBITS #number of bits per bytes
	ser1.parity = serial.PARITY_NONE #set parity check: no parity
	ser1.stopbits = serial.STOPBITS_ONE #number of stop bits
	#ser.timeout = None          #block read
	ser1.timeout = 1            #non-block read
	#ser.timeout = 2              #timeout block read
	ser1.xonxoff = False     #disable software flow control
	ser1.rtscts = False     #disable hardware (RTS/CTS) flow control
	ser1.dsrdtr = False       #disable hardware (DSR/DTR) flow control
	ser1.writeTimeout = 2     #timeout for write

	try: 
		ser1.open()
	except Exception as e:
		print ('error open serial port: ' + str(e))
		exit()
 
	if ser1.isOpen():
    
		try:
			ser1.flushInput() #flush input buffer, discarding all its contents
			ser1.flushOutput()#flush output buffer, aborting current output and discard all that is in buffer

			ser1.write(b'\x24\x06\xB0\x01\x23')					# changing the laser delay time to 0x01B0 -> 35us -> little endian 
			ser1.write(b'\x24\x07\x53\x02\x23')					# changing the laser width to 0x0253 -> 49.5us -> little endian 
			ser1.write(b'\x24\x08\xE0\x01\x23')					# changing the camera delay time to 0x01E0 -> 40us -> little endian 
			ser1.write(b'\x24\x09\xB0\x04\x23')					# changing the camera width to 0x04B0 -> 100us -> little endian -> \x78\xEA\ 
			rospy.loginfo("Time changed")
			time.sleep(0.5)
            
			while True:
				response = ser1.readline()
				print("read data:", response)
				
				numOfLines = numOfLines + 1

				if (numOfLines >= 5):
					break
		
		except Exception as e1:
			print ("error communicating...: " + str(e1))

	else:
		print ("cannot open serial port ")

	end_laser = time.time()
	print("laser time: " ,(end_laser - start_laser))

## Mirror function()
def initializeMirror():

	global Scuti1

	PORT = "/dev/ttyUSB0"

	#Configures the serial port
	Scuti1 = Scuti(port=PORT,timeout = 0.2)

	Scuti1.ser.write("start\r\n".encode())
	# print(Scuti1.ser.read(4))
	# print("initializing mirror")
	Scuti1.ser.write('reset\r\n'.encode())
	# time.sleep(0.05)
	# print(Scuti1.ser.read(4))


	
def trigger():

	global ser1
	global traffic
	print("trigger in")
	start = time.time()					# measuring the time the trigger takes
	if ser1.isOpen():
    
		try:
			ser1.flushInput() #flush input buffer, discarding all its contents
			ser1.flushOutput()#flush output buffer, aborting current output and discard all that is in buffer
			traffic = ser1.write(b'\x24\x01\x00\x00\x23')
			#print("traffic " ,traffic)
			#time.sleep(0.5)
            
			while True:
				response = ser1.readline()
				print("read data:", response)
				
				numOfLines = numOfLines + 1

				if (numOfLines >= 5):
					break
		
		except Exception as e1:
			print ("error communicating...: " + str(e1))

	else:
		print ("cannot open serial port ")

	traffic = 1
	end = time.time()
	print(end-start)
	print("trigger out")

def call_Mirror_Pattern(pattern):  				## trocar nome da variável data para evitar confusão

	global FOVhor
	global FOVvert
	global stephor
	global stepvert
	global offsetV
	global offsetH

	global start
	global init
	global stop
	global ready

	global negFOVH
	global negFOVV
	global negstepV

	print("receiving parameters")
	param=pattern.data																	#passes the mirror parameters
	FOVhor=param[0]
	rospy.loginfo(rospy.get_caller_id() + " FOVhor %d", FOVhor)
	FOVvert=param[1]
	rospy.loginfo(rospy.get_caller_id() + " FOVvert: %d", FOVvert)
	stephor=param[2]
	rospy.loginfo(rospy.get_caller_id() + " stephor: %d", stephor)
	stepvert=param[3]
	rospy.loginfo(rospy.get_caller_id() + " stepvert: %d", stepvert)
	offsetV = param[4]
	rospy.loginfo(rospy.get_caller_id() + " offsetvert: %d", offsetV)
	offsetH = param[5]
	rospy.loginfo(rospy.get_caller_id() + " offsethor: %d", offsetH)

	start=1																				
	init=0
	stop=0
	ready=1
 
	negFOVV = -FOVvert
	negFOVH = -FOVhor
	negstepV = -stepvert

	rospy.loginfo("negstepV: %f ",negstepV)
	rospy.loginfo("negFOVV: %f ",negFOVV)
	rospy.loginfo("negFOVH: %f",negFOVH)


def call_Stop(data):
	global stop
	stop=1
	Scuti1.ser.write('reset\r\n'.encode())
	rospy.loginfo("Waiting for new points...")
	print("stop")
def call_Quit(data):
	global ser1
	ser1.close()
	Scuti1.close()
	rospy.signal_shutdown("Shutting down. Bye...")
	print("quitting")
	
def call_Photo_Ready1(data):
	global photoReady1
	rospy.loginfo(rospy.get_caller_id() + "Photo_Ready1_test: %d", data.data)
	photoReady1=1
	print("receive photo 1")

def call_Photo_Ready2(data):
	global photoReady2
	#rospy.loginfo(rospy.get_caller_id() + "Photo_Ready2: %d", data.data)
	photoReady2=1
	print("receive photo 2")

def changePosition(position):
	global Scuti1
	global traffic
	global offsetV
	global offsetH

	# angleA = "angleA = {} deg\r\n".format(position[0])
	xx = position[0] + offsetH
	rospy.loginfo("position A: %d",xx)
	# angleB = "angleB = {} deg\r\n".format(position[1])
	yy = position[1] + offsetV
	rospy.loginfo("position B %d:",yy)
	angle2 = "2changle = {} deg; {}deg\r\n".format(xx,yy)
	
	Scuti1.ser.write(angle2.encode())

	print("changing position")
	
	while(Scuti1.ser.read(4) != 'OK\r\n'.encode()):
		print(Scuti1.ser.read(4))

	rospy.sleep(0.5)													# this sleep is very important 

	trigger()
    
	return 1

def call_trigger(data):
	
	rospy.loginfo("taking the trigger")

	rospy.sleep(0.5)

	trigger()

	return 1


def Mirror_Arduino():
	#rospy.init_node('Mirror_Arduino', anonymous=True)

	rospy.init_node ('Mirror_Arduino', anonymous=False, log_level = rospy.INFO, disable_signals = True)
	rospy.Subscriber("Mirror_Pattern", Float32MultiArray, call_Mirror_Pattern)
	rospy.Subscriber("Stop", Int8, call_Stop)
	rospy.Subscriber("Quit", Int8, call_Quit)
	rospy.Subscriber("take_photo", Int8, call_trigger)

	# rospy.Subscriber("image_raw_left", Int8, call_Photo_Ready1)
	# rospy.Subscriber("image_raw_right", Int8, call_Photo_Ready2)
	#pub1=rospy.Publisher('Activate_Trigger', Int8, queue_size=10)

	################
	rospy.Subscriber("Photo_Ready1", Int8, call_Photo_Ready1)
	rospy.Subscriber("Photo_Ready2", Int8, call_Photo_Ready2)
	################

	initializeLaser()
	rospy.loginfo("Laser was successfully initialized") 
	initializeMirror()
	rospy.loginfo("Mirror was successfully initialized") 

	position=[]
	x=0
	y=0
	k=0
	increment=0

	global photoReady1
	global photoReady2
	global FOVhor
	global FOVvert
	global stephor
	global stepvert
	global start
	global init
	global flag
	global stop
	global ready
	global negFOVH
	global negFOVV
	global negstepV

	yy = -1

	rate = rospy.Rate(1)
	while not rospy.is_shutdown():
		if init==0 and ready==1 and stop==0:     # ready=1, supõe que no inicio as cameras estão prontas para tirar foto
			if start==1 and ready==1:            #start=1, recebeu novos parametros e começa de novo
				rospy.loginfo("received new parameters")
				for x in arange(negFOVH,FOVhor+stephor,stephor):
					x = round(x,3)
					print(x)
					if(yy <=0):
						for y in arange(negFOVV,(FOVvert+stepvert),stepvert):
							y = round(y,3)
							position=[x,y]
							changePosition(position)			# changed the mirror position and activated the trigger
							yy = y
							print("x:", x)
							print("y:", y)
							print("yy: ",yy)

							if photoReady1 == 1 and photoReady2 == 1:
								rospy.loginfo("cameras took a photo")
								ready=1                 #cameras acabaram de tirar foto
								photoReady1=0
								photoReady2=0
								k=0
							else:
								ready=0                 #cameras não estão prontas para uma nova foto

					elif yy >0:
						for y in arange(FOVvert,(negFOVV+negstepV),negstepV):
							y = round(y,3)
							position=[x,y]
							changePosition(position)			# changed the mirror position and activated the trigger
							yy = y
							print("x:", x)
							print("y:", y)
							print("yy: ",yy)
							if photoReady1 == 1 and photoReady2 == 1:
								rospy.loginfo("cameras took a photo")
								ready=1                 #cameras acabaram de tirar foto
								photoReady1=0
								photoReady2=0
								k=0
							else:
								ready=0                 #cameras não estão prontas para uma nova foto
		rate.sleep()
	rospy.spin()

if __name__ == '__main__':
    try:
        Mirror_Arduino()
    except rospy.ROSInterruptException:
        pass