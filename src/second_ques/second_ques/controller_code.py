#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math
import time
#Definition of all the states
#0 → MOVE_STRAIGHT  
#1 → STOP_AFTER_STRAIGHT  
#2 → MOVE_ARC  
#3 → FINAL_STOP 

class Turtle_control_node(Node):
    def __init__(self):
        super().__init__("controller_node")
        self.state=0
        self.cmd_vel_publisher_=self.create_publisher(Twist, "/turtle1/cmd_vel",10)
        self.linear_v=2.0
        self.radius=2.0

        self.time_for_straight=(2*self.radius)/self.linear_v
        self.time_for_arc=(math.pi*self.radius)/self.linear_v

        self.start_time=time.time()
        self.timer = self.create_timer(0.05, self.control_loop)
        self.get_logger().info("Starting D-shape motion")

    def control_loop(self):
        data=Twist()
        time_gone=time.time()-self.start_time
        if(self.state==0):
            data.linear.x=self.linear_v
            data.angular.z=0.0
            if(time_gone>=self.time_for_straight):
                self.state=1
                self.start_time=time.time()
                self.get_logger().info("Finished straight line")
        elif(self.state==1):
            data.linear.x=0.0
            data.angular.z=0.0
            if time_gone>=0.5:
                self.state=2
                self.start_time=time.time()
                self.get_logger().info("Going to start the semicircle")
        elif(self.state==2):
            data.linear.x=0.0
            data.angular.z=math.pi/2
            if(time_gone>=1.0):
                self.state=3
                self.start_time=time.time()
        elif(self.state==3):
            data.linear.x=self.linear_v
            data.angular.z=self.linear_v/self.radius
            if(time_gone>=2.0):
                self.get_logger().info("Finished the D shape")
                self.timer.cancel() #To stop the execution
        self.cmd_vel_publisher_.publish(data)
        

def main(args=None):
    rclpy.init(args=args)
    node=Turtle_control_node()
    rclpy.spin(node)
    rclpy.shutdown()
