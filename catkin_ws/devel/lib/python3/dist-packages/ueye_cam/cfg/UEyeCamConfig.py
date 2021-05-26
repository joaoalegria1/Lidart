## *********************************************************
##
## File autogenerated for the ueye_cam package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'name': 'Default', 'type': '', 'state': True, 'cstate': 'true', 'id': 0, 'parent': 0, 'parameters': [{'name': 'image_width', 'type': 'int', 'default': 640, 'level': 1, 'description': "Width of camera's area of interest (prior to subsampling, binning, or sensor scaling)", 'min': 16, 'max': 4912, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'image_height', 'type': 'int', 'default': 480, 'level': 1, 'description': "Height of camera's area of interest (prior to subsampling, binning, or sensor scaling)", 'min': 4, 'max': 3684, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'image_left', 'type': 'int', 'default': -1, 'level': 1, 'description': "Left index for camera's area of interest (-1: center)", 'min': -1, 'max': 2544, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'image_top', 'type': 'int', 'default': -1, 'level': 1, 'description': "Top index for camera's area of interest (-1: center)", 'min': -1, 'max': 1916, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'color_mode', 'type': 'str', 'default': 'mono8', 'level': 1, 'description': 'Output image color mode', 'min': '', 'max': '', 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': "{'enum': [{'name': 'MONO8', 'type': 'str', 'value': 'mono8', 'srcline': 22, 'srcfile': '/home/lidart/catkin_ws/src/ueye_cam/cfg/UEyeCam.cfg', 'description': '8-bit Monochrome', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'MONO10', 'type': 'str', 'value': 'mono10', 'srcline': 23, 'srcfile': '/home/lidart/catkin_ws/src/ueye_cam/cfg/UEyeCam.cfg', 'description': '10-bit Monochrome', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'MONO12', 'type': 'str', 'value': 'mono12', 'srcline': 24, 'srcfile': '/home/lidart/catkin_ws/src/ueye_cam/cfg/UEyeCam.cfg', 'description': '12-bit Monochrome', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'MONO16', 'type': 'str', 'value': 'mono16', 'srcline': 25, 'srcfile': '/home/lidart/catkin_ws/src/ueye_cam/cfg/UEyeCam.cfg', 'description': '16-bit Monochrome', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'RGB8', 'type': 'str', 'value': 'rgb8', 'srcline': 26, 'srcfile': '/home/lidart/catkin_ws/src/ueye_cam/cfg/UEyeCam.cfg', 'description': '24-bit Red/Green/Blue', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'RGB10', 'type': 'str', 'value': 'rgb10', 'srcline': 27, 'srcfile': '/home/lidart/catkin_ws/src/ueye_cam/cfg/UEyeCam.cfg', 'description': '32-bit packed Red/Green/Blue', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'RGB10u', 'type': 'str', 'value': 'rgb10u', 'srcline': 28, 'srcfile': '/home/lidart/catkin_ws/src/ueye_cam/cfg/UEyeCam.cfg', 'description': '48-bit unpacked Red/Green/Blue', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'RGB12u', 'type': 'str', 'value': 'rgb12u', 'srcline': 29, 'srcfile': '/home/lidart/catkin_ws/src/ueye_cam/cfg/UEyeCam.cfg', 'description': '48-bit unpacked Red/Green/Blue', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'BGR8', 'type': 'str', 'value': 'bgr8', 'srcline': 30, 'srcfile': '/home/lidart/catkin_ws/src/ueye_cam/cfg/UEyeCam.cfg', 'description': '24-bit Blue/Green/Red', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'BGR10', 'type': 'str', 'value': 'bgr10', 'srcline': 31, 'srcfile': '/home/lidart/catkin_ws/src/ueye_cam/cfg/UEyeCam.cfg', 'description': '32-bit packed Blue/Green/Red', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'BGR10u', 'type': 'str', 'value': 'bgr10u', 'srcline': 32, 'srcfile': '/home/lidart/catkin_ws/src/ueye_cam/cfg/UEyeCam.cfg', 'description': '48-bit unpacked Blue/Green/Red', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'BGR12u', 'type': 'str', 'value': 'bgr12u', 'srcline': 33, 'srcfile': '/home/lidart/catkin_ws/src/ueye_cam/cfg/UEyeCam.cfg', 'description': '48-bit unpacked Blue/Green/Red', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'BAYER_RGGB8', 'type': 'str', 'value': 'bayer_rggb8', 'srcline': 34, 'srcfile': '/home/lidart/catkin_ws/src/ueye_cam/cfg/UEyeCam.cfg', 'description': '8-bit Raw Bayer (RGGB)', 'ctype': 'std::string', 'cconsttype': 'const char * const'}], 'enum_description': 'Color mode values'}", 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'subsampling', 'type': 'int', 'default': 1, 'level': 1, 'description': 'Output image subsampling ratio', 'min': -2147483648, 'max': 2147483647, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': "{'enum': [{'name': 'SUB_1X', 'type': 'int', 'value': 1, 'srcline': 40, 'srcfile': '/home/lidart/catkin_ws/src/ueye_cam/cfg/UEyeCam.cfg', 'description': '1X Subsampling', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'SUB_2X', 'type': 'int', 'value': 2, 'srcline': 41, 'srcfile': '/home/lidart/catkin_ws/src/ueye_cam/cfg/UEyeCam.cfg', 'description': '2X Subsampling', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'SUB_4X', 'type': 'int', 'value': 4, 'srcline': 42, 'srcfile': '/home/lidart/catkin_ws/src/ueye_cam/cfg/UEyeCam.cfg', 'description': '4X Subsampling', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'SUB_8X', 'type': 'int', 'value': 8, 'srcline': 43, 'srcfile': '/home/lidart/catkin_ws/src/ueye_cam/cfg/UEyeCam.cfg', 'description': '8X Subsampling', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'SUB_16X', 'type': 'int', 'value': 16, 'srcline': 44, 'srcfile': '/home/lidart/catkin_ws/src/ueye_cam/cfg/UEyeCam.cfg', 'description': '16X Subsampling', 'ctype': 'int', 'cconsttype': 'const int'}], 'enum_description': 'Subsampling Values'}", 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'binning', 'type': 'int', 'default': 1, 'level': 1, 'description': 'Output image binning ratio', 'min': -2147483648, 'max': 2147483647, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': "{'enum': [{'name': 'BIN_1X', 'type': 'int', 'value': 1, 'srcline': 50, 'srcfile': '/home/lidart/catkin_ws/src/ueye_cam/cfg/UEyeCam.cfg', 'description': '1X Binning', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'BIN_2X', 'type': 'int', 'value': 2, 'srcline': 51, 'srcfile': '/home/lidart/catkin_ws/src/ueye_cam/cfg/UEyeCam.cfg', 'description': '2X Binning', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'BIN_4X', 'type': 'int', 'value': 4, 'srcline': 52, 'srcfile': '/home/lidart/catkin_ws/src/ueye_cam/cfg/UEyeCam.cfg', 'description': '4X Binning', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'BIN_8X', 'type': 'int', 'value': 8, 'srcline': 53, 'srcfile': '/home/lidart/catkin_ws/src/ueye_cam/cfg/UEyeCam.cfg', 'description': '8X Binning', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'BIN_16X', 'type': 'int', 'value': 16, 'srcline': 54, 'srcfile': '/home/lidart/catkin_ws/src/ueye_cam/cfg/UEyeCam.cfg', 'description': '16X Binning', 'ctype': 'int', 'cconsttype': 'const int'}], 'enum_description': 'Binning Values'}", 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'sensor_scaling', 'type': 'double', 'default': 1.0, 'level': 1, 'description': 'Output image scaling ratio (Internal Image Scaling)', 'min': -inf, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': "{'enum': [{'name': 'SS_1X', 'type': 'double', 'value': 1.0, 'srcline': 60, 'srcfile': '/home/lidart/catkin_ws/src/ueye_cam/cfg/UEyeCam.cfg', 'description': '1X Internal Image Scaling', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'SS_2X', 'type': 'double', 'value': 2.0, 'srcline': 61, 'srcfile': '/home/lidart/catkin_ws/src/ueye_cam/cfg/UEyeCam.cfg', 'description': '2X Internal Image Scaling', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'SS_4X', 'type': 'double', 'value': 4.0, 'srcline': 62, 'srcfile': '/home/lidart/catkin_ws/src/ueye_cam/cfg/UEyeCam.cfg', 'description': '4X Internal Image Scaling', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'SS_8X', 'type': 'double', 'value': 8.0, 'srcline': 63, 'srcfile': '/home/lidart/catkin_ws/src/ueye_cam/cfg/UEyeCam.cfg', 'description': '8X Internal Image Scaling', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'SS_16X', 'type': 'double', 'value': 16.0, 'srcline': 64, 'srcfile': '/home/lidart/catkin_ws/src/ueye_cam/cfg/UEyeCam.cfg', 'description': '16X Internal Image Scaling', 'ctype': 'double', 'cconsttype': 'const double'}], 'enum_description': 'Internal Image Scaling Values'}", 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'auto_gain', 'type': 'bool', 'default': False, 'level': 0, 'description': 'Auto gain (overruled by auto framerate)', 'min': False, 'max': True, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'bool', 'cconsttype': 'const bool'}, {'name': 'master_gain', 'type': 'int', 'default': 0, 'level': 0, 'description': 'Master gain percentage', 'min': 0, 'max': 100, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'red_gain', 'type': 'int', 'default': 0, 'level': 0, 'description': 'Gain percentage for red channel', 'min': 0, 'max': 100, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'green_gain', 'type': 'int', 'default': 0, 'level': 0, 'description': 'Gain percentage for green channel', 'min': 0, 'max': 100, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'blue_gain', 'type': 'int', 'default': 0, 'level': 0, 'description': 'Gain percentage for blue channel', 'min': 0, 'max': 100, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'gain_boost', 'type': 'bool', 'default': False, 'level': 0, 'description': 'Analog gain boost', 'min': False, 'max': True, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'bool', 'cconsttype': 'const bool'}, {'name': 'auto_exposure', 'type': 'bool', 'default': False, 'level': 0, 'description': 'Auto exposure (a.k.a. auto shutter)', 'min': False, 'max': True, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'bool', 'cconsttype': 'const bool'}, {'name': 'exposure', 'type': 'double', 'default': 33.0, 'level': 0, 'description': 'Exposure value (ms)', 'min': 0.0, 'max': 300.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'auto_white_balance', 'type': 'bool', 'default': False, 'level': 0, 'description': 'Auto white balance', 'min': False, 'max': True, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'bool', 'cconsttype': 'const bool'}, {'name': 'white_balance_red_offset', 'type': 'int', 'default': 0, 'level': 0, 'description': 'Red level offset for white balance', 'min': -50, 'max': 50, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'white_balance_blue_offset', 'type': 'int', 'default': 0, 'level': 0, 'description': 'Blue level offset for white balance', 'min': -50, 'max': 50, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'flash_delay', 'type': 'int', 'default': 0, 'level': 0, 'description': 'Flash output delay (us) [not applicable in external trigger mode]', 'min': -1000000, 'max': 1000000, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'flash_duration', 'type': 'int', 'default': 1000, 'level': 0, 'description': 'Flash output duration (us) (0: set to exposure duration) [not applicable in external trigger mode]', 'min': 0, 'max': 1000000, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'ext_trigger_mode', 'type': 'bool', 'default': False, 'level': 1, 'description': 'Toggle between external trigger mode and free-run mode', 'min': False, 'max': True, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'bool', 'cconsttype': 'const bool'}, {'name': 'auto_frame_rate', 'type': 'bool', 'default': False, 'level': 0, 'description': 'Auto frame rate (requires auto exposure, supercedes auto gain) [not applicable in external trigger mode]', 'min': False, 'max': True, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'bool', 'cconsttype': 'const bool'}, {'name': 'frame_rate', 'type': 'double', 'default': 10.0, 'level': 0, 'description': 'Frame process rate (Hz) [not applicable in external trigger mode]', 'min': 0.01, 'max': 200.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'output_rate', 'type': 'double', 'default': 0.0, 'level': 0, 'description': 'Frame publish rate (Hz) (0: publish all processed frames) [not applicable in external trigger mode]', 'min': 0.0, 'max': 200.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'pixel_clock', 'type': 'int', 'default': 25, 'level': 0, 'description': 'Pixel clock (MHz)', 'min': 1, 'max': 500, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'flip_upd', 'type': 'bool', 'default': False, 'level': 0, 'description': 'Mirror Upside Down', 'min': False, 'max': True, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'bool', 'cconsttype': 'const bool'}, {'name': 'flip_lr', 'type': 'bool', 'default': False, 'level': 0, 'description': 'Mirror Left Right', 'min': False, 'max': True, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'bool', 'cconsttype': 'const bool'}], 'groups': [], 'srcline': 246, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'class': 'DEFAULT', 'parentclass': '', 'parentname': 'Default', 'field': 'default', 'upper': 'DEFAULT', 'lower': 'groups'}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

UEyeCam_MONO8 = 'mono8'
UEyeCam_MONO10 = 'mono10'
UEyeCam_MONO12 = 'mono12'
UEyeCam_MONO16 = 'mono16'
UEyeCam_RGB8 = 'rgb8'
UEyeCam_RGB10 = 'rgb10'
UEyeCam_RGB10u = 'rgb10u'
UEyeCam_RGB12u = 'rgb12u'
UEyeCam_BGR8 = 'bgr8'
UEyeCam_BGR10 = 'bgr10'
UEyeCam_BGR10u = 'bgr10u'
UEyeCam_BGR12u = 'bgr12u'
UEyeCam_BAYER_RGGB8 = 'bayer_rggb8'
UEyeCam_SUB_1X = 1
UEyeCam_SUB_2X = 2
UEyeCam_SUB_4X = 4
UEyeCam_SUB_8X = 8
UEyeCam_SUB_16X = 16
UEyeCam_BIN_1X = 1
UEyeCam_BIN_2X = 2
UEyeCam_BIN_4X = 4
UEyeCam_BIN_8X = 8
UEyeCam_BIN_16X = 16
UEyeCam_SS_1X = 1.0
UEyeCam_SS_2X = 2.0
UEyeCam_SS_4X = 4.0
UEyeCam_SS_8X = 8.0
UEyeCam_SS_16X = 16.0
