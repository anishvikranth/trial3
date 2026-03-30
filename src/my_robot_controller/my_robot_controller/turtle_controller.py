#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtlesim.srv import SetPen
from functools import partial
class TurtleControllerNode(Node):
    def __init__(self):
        super().__init__("turtle_controller_node")
        self.prevx=0
        self.cmd_vel_publisher_=self.create_publisher(Twist, "/turtle1/cmd_vel",10)
        self.listen_pub_=self.create_subscription(Pose,"/turtle1/pose",self.pose_callback,10)
        self.get_logger().info("Turtle controller has been started")

    def pose_callback(self,pose:Pose):
        cmd=Twist()
        #on checking practically we get the ends at 11.08 
        if(pose.x>9.0 or pose.x<2.0 or pose.y>9.0 or pose.y<2.0):
            cmd.angular.z=0.9
            cmd.linear.x=1.0
        else:
            cmd.angular.z=0.0
            cmd.linear.x=5.0
        
        self.cmd_vel_publisher_.publish(cmd)

        if (pose.x>5.5 and self.prevx<=5.5):
            self.prevx=pose.x
            self.get_logger().info("Color changed to red")
            self.call_set_pen_service(255,0,0,3,0)
        elif(pose.x<=5.5 and self.prevx>5.5):
            self.prevx=pose.x
            self.get_logger().info("Color changed to green")
            self.call_set_pen_service(0,255,0,3,0)
    
    def call_set_pen_service(self,r,g,b,width,off):
        client=self.create_client(SetPen,"/turtle1/set_pen")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for the service ....")
        request=SetPen.Request()
        request.r=r
        request.g=g
        request.b=b
        request.width=width
        request.off=off

        future=client.call_async(request)
        future.add_done_callback(partial(self.callback)) #Partial lets you prefill the arguments for a function,
    def callback(self,future):
        try:
            response=future.result()
        except Exception as e:
            self.get_logger().error("Service call failed %r"%(e,))

def main(args=None):
    rclpy.init(args=args)
    node=TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()

