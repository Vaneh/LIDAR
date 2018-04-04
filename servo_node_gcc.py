#!/usr/bin/env python
import os #1 
from lib_robotis import * #2
import os.path 

import rospy
from std_msgs.msg import String
from servo_lidar_test.msg import Num
from servo_lidar_test.msg import servo
 
dyn = USB2Dynamixel_Device('/dev/ttyUSB0')
p = Robotis_Servo( dyn, 1, series = "MX" )
#p.set_angvel(0.8)



def main():

    define_publish_rate = 6000 
    count1= 3000 #in bits
    count2= 2000 # in bits
    
    home = 0 # in radians
    servo_speed = 0.2 # radians/sec

    pub = rospy.Publisher('chatter', String, queue_size=10)
    servo_pub = rospy.Publisher('servo_cmd', servo, queue_size=10)

    #rospy.Subscriber("custom_chatter", Num, callbackThree)
    

    rospy.init_node('servo_test')
    
    rate = rospy.Rate(define_publish_rate)

    msg3 = servo()
    
    count = 0
    
    p.move_angle(home)
    p.set_angvel(servo_speed)

    while not rospy.is_shutdown():
      
        

        while count < count1:
           msg3.servoAngle = p.read_angle()
           p.move_to_encoder(4000)
           count = p.read_encoder()
           servo_pub.publish(msg3)
           #rospy.loginfo(count)


        while count > count2:  
           msg3.servoAngle = p.read_angle()
           p.move_to_encoder(1000)
           count = p.read_encoder()
           servo_pub.publish(msg3)
           #rospy.loginfo(count)

         # for i in range(4,2040):
         #     p.move_to_encoder(i)
         #     msg3.servoAngle = p.read_angle()
         #     pub.publish(msg3)



        
         # t.secs=10
         #pub2.publish(msg3)
         #rospy.loginfo(msg3)
        rate.sleep()

        
     
    p.kill_cont_turn()    
    rospy.spin()



if __name__ == '__main__':
           
        main()