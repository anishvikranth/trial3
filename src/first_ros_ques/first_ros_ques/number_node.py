#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int8

class numbNodes(Node):
    def __init__(self):
        super().__init__("number_node")
        self.prevNo=0
        self.numb_publish=self.create_publisher(Int8,'/number',10)
        self.numb_subscribe=self.create_subscription(Int8,'/count',self.numb_subsci,10)
        self.timer = self.create_timer(1.0, self.timer_callback) #To make sure the deadlock is surpassed
    def numb_subsci(self,kilo:Int8):
        input_count=kilo.data
        msg=Int8()
        if(input_count<self.prevNo):
            msg.data=self.prevNo
        elif(input_count>=self.prevNo):
            self.prevNo+=1
            msg.data=self.prevNo
        self.numb_publish.publish(msg)
        self.get_logger().info(f"Number: {self.prevNo}, Count: {input_count}") #Note the count is the count received to the funtion
        #not the count of the actual new number
    def timer_callback(self):
       msg = Int8()
       msg.data = self.prevNo   # initial n (0)
       self.numb_publish.publish(msg)
       self.get_logger().info(f"Initial publish: {self.prevNo}")
       self.timer.cancel() #Stop the timer after the first publish

def main(args=None):
    rclpy.init(args=args)
    node=numbNodes()
    rclpy.spin(node)
    rclpy.shutdown()
