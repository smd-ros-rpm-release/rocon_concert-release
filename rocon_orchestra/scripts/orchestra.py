#!/usr/bin/env python

import roslib; roslib.load_manifest('rocon_orchestra')
import rospy

from ros import rocon_orchestra


if __name__ == '__main__':
    rocon_orchestra.orchestration.main()
