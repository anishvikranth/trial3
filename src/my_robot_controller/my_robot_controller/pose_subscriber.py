#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
class subscriber_node(Node):
    def __init__(self):
        super().__init__("pose_subscriber")
        self.listen_pub_=self.create_subscription(Pose,"/turtle1/pose",self.reading_func,10)
        #Unlike the publishing example, we have to also include the callback function 
        
    
    def reading_func(self,msg:Pose):
      self.get_logger().info("("+str(msg.x)+","+str(msg.y)+")")

def main(args=None):
    rclpy.init(args=args)
    node=subscriber_node()
    rclpy.spin(node)
    rclpy.shutdown()
