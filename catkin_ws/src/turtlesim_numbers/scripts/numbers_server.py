#!/usr/bin/env python

from turtlesim_numbers.srv import Numbers,NumbersResponse
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time
from std_srvs.srv import Empty

x=0
y=0
yaw=0

def poseCallback(pose_message):
    global x
    global y, yaw
    x= pose_message.x
    y= pose_message.y
    yaw = pose_message.theta


def move(speed, distance, is_forward):
        #declare a Twist message to send velocity commands
        velocity_message = Twist()
        #get current location 
        global x, y
        x0=x
        y0=y

        if (is_forward):
            velocity_message.linear.x =abs(speed)
        else:
        	velocity_message.linear.x =-abs(speed)

        distance_moved = 0.0
        loop_rate = rospy.Rate(10) # we publish the velocity at 10 Hz (10 times a second)    
        cmd_vel_topic='/turtle1/cmd_vel'
        velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)

        while True :
                rospy.loginfo("Turtlesim moves forwards")
                velocity_publisher.publish(velocity_message)
                loop_rate.sleep()
                distance_moved = abs(0.5 * math.sqrt(((x-x0) ** 2) + ((y-y0) ** 2)))
                print  distance_moved               
                if  not (distance_moved<distance):
                    rospy.loginfo("reached")
                    break
        
        #finally, stop the robot when the distance is moved
        velocity_message.linear.x =0
        velocity_publisher.publish(velocity_message)

def rotate (angular_speed_degree, relative_angle_degree, clockwise):
    
    global yaw
    velocity_message = Twist()
    velocity_message.linear.x=0
    velocity_message.linear.y=0
    velocity_message.linear.z=0
    velocity_message.angular.x=0
    velocity_message.angular.y=0
    velocity_message.angular.z=0

    #get current location 
    theta0=yaw
    angular_speed=math.radians(abs(angular_speed_degree))

    if (clockwise):
        velocity_message.angular.z =-abs(angular_speed)
    else:
        velocity_message.angular.z =abs(angular_speed)

    angle_moved = 0.0
    loop_rate = rospy.Rate(10) # we publish the velocity at 10 Hz (10 times a second)    
    cmd_vel_topic='/turtle1/cmd_vel'
    velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)

    t0 = rospy.Time.now().to_sec()

    while True :
        rospy.loginfo("Turtlesim rotates")
        velocity_publisher.publish(velocity_message)

        t1 = rospy.Time.now().to_sec()
        current_angle_degree = (t1-t0)*angular_speed_degree
        loop_rate.sleep()


                       
        if  (current_angle_degree>relative_angle_degree):
            rospy.loginfo("reached")
            break

    #finally, stop the robot when the distance is moved
    velocity_message.angular.z =0
    velocity_publisher.publish(velocity_message)

def setDesiredOrientation(desired_angle_radians):
    relative_angle_radians = desired_angle_radians - yaw
    if relative_angle_radians < 0:
        clockwise = 1
    else:
        clockwise = 0
    print relative_angle_radians
    print desired_angle_radians
    rotate(1 ,math.degrees(abs(relative_angle_radians)), clockwise)



def one():
    setDesiredOrientation(math.pi/2)
    move(1.0,2.0,True)
    move(1.0,4.0,False)

def two():
    move(1.0,1.0,True)
    setDesiredOrientation(math.pi/2)
    move(1.0,2.0,True)
    setDesiredOrientation(math.pi)
    move(1.0,2.0,True)
    move(1.0,2.0,False)
    setDesiredOrientation(math.pi/2)
    move(1.0,2.0,False)
    setDesiredOrientation(math.pi)
    move(1.0,2.0,True)
    setDesiredOrientation(3*math.pi/2)
    move(1.0,2.0,True)
    setDesiredOrientation(0)
    move(1.0,2.0,True)

def four():
    setDesiredOrientation(math.pi/2)
    move(1.0,2.0,True)
    move(1.0,4.0,False)
    move(1.0,2.0,True)
    setDesiredOrientation(math.pi)
    move(1.0,2.0,True)
    setDesiredOrientation(math.pi/2)
    move(1.0,2.0,True)

def five():
    move(1.0,1.0,True)
    setDesiredOrientation(-math.pi/2)
    move(1.0,2.0,True)
    setDesiredOrientation(-math.pi)
    move(1.0,2.0,True)
    move(1.0,2.0,False)
    setDesiredOrientation(math.pi/2)
    move(1.0,2.0,True)
    setDesiredOrientation(math.pi)
    move(1.0,2.0,True)
    setDesiredOrientation(math.pi/2)
    move(1.0,2.0,True)
    setDesiredOrientation(0)
    move(1.0,2.0,True)

def eight():
    move(1.0,1.0,True)
    setDesiredOrientation(math.pi/2)
    move(1.0,2.0,True)
    setDesiredOrientation(math.pi)
    move(1.0,2.0,True)
    setDesiredOrientation(-math.pi/2)
    move(1.0,4,0,True)
    setDesiredOrientation(0)
    move(1.0,2.0,True)
    setDesiredOrientation(math.pi/2)
    move(1.0,2.0,True)
    setDesiredOrientation(math.pi)
    move(1.0,2.0,True)

def seven():
    setDesiredOrientation(math.pi/2)
    move(1.0,2.0,False)
    move(1.0,4.0,True)
    setDesiredOrientation(math.pi)
    move(1.0,2.0,True)



def zero():
    setDesiredOrientation(math.pi/2)
    move(1.0, 2.0, True)
    setDesiredOrientation(math.pi)
    move(1.0, 2.0, True)
    setDesiredOrientation(-math.pi/2)
    move(1.0, 4.0, True)
    setDesiredOrientation(0)
    move(1.0, 2.0, True)
    setDesiredOrientation(math.pi/2)
    move(1.0, 2.0, True)

def three():
    move(1.0, 2.0, True)
    setDesiredOrientation(math.pi/2)
    move(1.0, 2.0, True)
    setDesiredOrientation(math.pi)
    move(1.0, 2.0, True)
    move(1.0, 2.0, False)
    setDesiredOrientation(math.pi/2)
    move(1.0, 4.0, False)
    setDesiredOrientation(math.pi)
    move(1.0, 2.0, True)

def six():
    setDesiredOrientation(-math.pi/2)
    move(1.0, 2.0, True)
    setDesiredOrientation(math.pi)
    move(1.0, 2.0, True)
    setDesiredOrientation(math.pi/2)
    move(1.0, 2.0, True)
    setDesiredOrientation(0)
    move(1.0, 2.0, True)
    move(1.0, 2.0, False)
    setDesiredOrientation(math.pi/2)
    move(1.0, 2.0, True)
    setDesiredOrientation(0)
    move(1.0, 2.0, True)

def nine():
    setDesiredOrientation(math.pi/2)
    move(1.0, 2.0, True)
    setDesiredOrientation(math.pi)
    move(1.0, 2.0, True)
    setDesiredOrientation(-math.pi/2)
    move(1.0, 2.0, True)
    setDesiredOrientation(0)
    move(1.0, 2.0, True)
    setDesiredOrientation(-math.pi/2)
    move(1.0, 2.0, True)
    setDesiredOrientation(math.pi)
    move(1.0, 2.0, True)

    


def handle_numbers(req):
    print "Printing your number"
    try:
        #declare velocity publisher
        cmd_vel_topic='/turtle1/cmd_vel'
        velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)
        
        position_topic = "/turtle1/pose"
        pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback) 
        time.sleep(2)
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")
    
    if (req.a==0):    
        zero()
    if (req.a==1):
        one()
    if (req.a==2):
        two()
    if (req.a==3):
        three()
    if (req.a==4):
        four()
    if (req.a==5):
        five()
    if (req.a==6):
        six()
    if (req.a==7):
        seven()
    if (req.a==8):
        eight()
    if (req.a==9):
        nine()
    return NumbersResponse(req.a + req.b)

def numbers_server():
    rospy.init_node('numbers_server')
    s = rospy.Service('numbers', Numbers, handle_numbers)
    print "Ready to print number"
    rospy.spin()

if __name__ == "__main__":    
    numbers_server()






        

