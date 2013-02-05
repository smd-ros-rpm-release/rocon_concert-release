#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_concert/concert_master/LICENSE
#
##############################################################################
# Imports
##############################################################################

import rospy
from concert_master import ConcertMaster

##############################################################################
# Main
##############################################################################

if __name__ == '__main__':
    rospy.init_node('concert_master')

    cm = ConcertMaster()
    rospy.loginfo("Initialised")
    cm.spin()
