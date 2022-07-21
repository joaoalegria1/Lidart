#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
This program is used to trigger the cameras using ROS publisher and subscribers
21/07/2022 - Creation of the file
'''

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


def CameraTrigger():
	#rospy.init_node('Mirror_Arduino', anonymous=True)

	rospy.init_node ('CameraTrigger', anonymous=False, log_level = rospy.INFO, disable_signals = True)
	rospy.Subscriber("Stop", Int8, call_Stop)
	rospy.Subscriber("Quit", Int8, call_Quit)
	rospy.Subscriber("take_photo", Int8, call_trigger)

	################
	rospy.Subscriber("Photo_Ready1", Int8, call_Photo_Ready1)
	rospy.Subscriber("Photo_Ready2", Int8, call_Photo_Ready2)
	################


if __name__ == '__main__':
    try:
        CameraTrigger()
    except rospy.ROSInterruptException:
        pass