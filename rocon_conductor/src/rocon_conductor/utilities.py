'''
Utility functions.

'''
import roslib; roslib.load_manifest('rocon_conductor')
from concert_comms.msg import *

##############################################################################
# Utilities
##############################################################################

def platform_id_to_string(platform_id):
    '''
      Platform info to string converter
      
      This should be in a shared location (alongside concert_comms probably) rather than
      buried here in a user of the concert_comms.PlatformInfo module.
    '''
    if platform_id == concert_comms.msg.PlatformInfo.PLATFORM_LINUX:
        s = "linux"
    elif platform_id == concert_comms.msg.PlatformInfo.PLATFORM_ANDROID:
        s = "android"
    elif platform_id == concert_comms.msg.PlatformInfo.PLATFORM_WINDOZE:
        s = "windows"
    else:
        s = "unknown"
    return s

def system_id_to_string(system_id):
    '''
      System info to string converter
      
      This should be in a shared location (alongside concert_comms probably) rather than
      buried here in a user of the concert_comms.PlatformInfo module.
    '''
    if system_id == concert_comms.msg.PlatformInfo.SYSTEM_ROS:
        s = "ros"
    elif system_id == concert_comms.msg.PlatformInfo.SYSTEM_OPROS:
        s = "opros"
    else:
        s = "unknown"
    return s

