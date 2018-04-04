#!/usr/bin/env python
import rospy
import math
import sys

from sensor_msgs.msg import PointCloud2
import std_msgs.msg
import sensor_msgs.point_cloud2 as pcl2
from servo_lidar_test.msg import controller

x = 0
y = 0
z = 0

def callbackForCordinates(msg):

    global x
    global y
    global z

    x = msg.x
    y = msg.y
    z = msg.z




if __name__ == '__main__':
    '''
    Sample code to publish a pcl2 with python
    '''
    rospy.init_node('pcl2_pub_example')

    rate = rospy.Rate(6000)  # The while loop rate

    rospy.Subscriber('controller', controller, callbackForCordinates) # Subscribes to Adriks lidar

    pcl_pub = rospy.Publisher("/my_pcl_topic", PointCloud2, queue_size=10)
    rospy.loginfo("Initializing sample pcl2 publisher node...")
    
    #give time to roscore to make the connections
    rospy.sleep(1.)
    
    
    
    #header
    header = std_msgs.msg.Header()
    header.stamp = rospy.Time.now()
    header.frame_id = 'map'
    
    
    
    
    
    #publish    
    rospy.loginfo("happily publishing sample pointcloud.. !")
    count = 0
    cloud_points = [[0,0,0],[1,1,1]]
    while not rospy.is_shutdown():
        #count += 1



        #x1 = math.sin(count)
        #x2 = math.sin(count + math.pi)

        
        #cloud_points = [[x1, 1.0, 1.0],[x2, 2.0, 0.0]]
        cloud_points.append([x, y, z])





        #create pcl from points
        scaled_polygon_pcl = pcl2.create_cloud_xyz32(header, cloud_points)

        pcl_pub.publish(scaled_polygon_pcl)

        rate.sleep()

        

