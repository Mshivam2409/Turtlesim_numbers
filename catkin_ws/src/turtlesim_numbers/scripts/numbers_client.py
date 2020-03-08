#!/usr/bin/env python

import sys
import rospy
from turtlesim_numbers.srv import *

def numbers_client(x, y):
    rospy.wait_for_service('numbers')
    try:
        numbers = rospy.ServiceProxy('numbers', Numbers)
        resp1 = numbers(x, y)
        return resp1.sum
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    y = 0
    x = int(input("Enter your number"))
    print "Printing your number %s "%(numbers_client(x,y))
    # print "%s + %s = %s"%(x, y, s)