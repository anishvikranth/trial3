#!/usr/bin/env python3      
#The above line is called the shebang line, tells the linux to run the file using python 3
import rclpy #Provides the functions to nodes,communication with ROS
from rclpy.node import Node
class myNode(Node):
    def __init__(self): #Used to initialize the node
        super().__init__("first_node")

        self.counter=0
        self.create_timer(1.0, self.callback)
    def callback(self):
        self.get_logger().info("Hello"+str(self.counter))
        self.counter +=1
def main(args=None):
    rclpy.init(args=args)  #To initialise the ros2 communications
    
    #Node will be created inside the program
    node=myNode()
    rclpy.spin(node) #THis Command is used to run the node again and again
    rclpy.shutdown()

if __name__ == '_main_':
    main()