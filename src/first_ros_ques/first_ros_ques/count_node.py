#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int8
class CountNodes(Node):
    def __init__(self):
        super().__init__("count_node")
        self.count=0
        self.num_prev=0
        self.count_publisher=self.create_publisher(Int8,'/count',10)
        self.count_subscriber=self.create_subscription(Int8,'/number',self.subi_func,10)
    
    def subi_func(self, num: Int8):
        input_no=num.data
        if(input_no!=self.num_prev):
          self.count=0
        self.count+=1 
        msg = Int8()
        msg.data=self.count
        self.count_publisher.publish(msg)
        self.num_prev=input_no
        self.get_logger().info(f"Number: {input_no}, Count: {self.count}")

        
def main(args=None):
    rclpy.init(args=args)
    node=CountNodes()
    rclpy.spin(node)
    rclpy.shutdown()