#!/usr/bin/env python3

import rclpy
import time
from rclpy.node import Node

from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool

class JoyToCmdVel(Node):
    def __init__(self):
        super().__init__('joy_to_cmd_vel')
        self.cmd_vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.joy_sub = self.create_subscription(Joy, 'joy', self.joy_callback, 10)
        self.publisher = self.create_publisher(Bool, "/catch_trigger", 10)
        self.linear_scale = 0.5
        self.angular_scale = 1.
        self.button = [0,0,0,0,0,0,0,0,0,0,0]  # A, B,Y,Z, LH , RH , back, start, ?, L3, R3
        self.Jaxes = [0,0,0,0,0,0,0,0]   # (gauche gauche(1)/droite(-1), gauche haut(1)/bas(-1), ? , droite gauche(1)/droite(-1), droite haut(1)/bas(-1), ?, flèches gauche(1)/droite(-1), flèches haut(1)/bas(-1))
        self.frame_id = 0
        self.frame_id_old = 0
        self.bool = Bool()
        self.bool.data = False

    def joy_callback(self, msg):
        twist = Twist()
        self.button = msg.buttons
        self.Jaxes = msg.axes
        self.frame_id = msg.header.stamp
        twist.linear.x = self.linear_scale * msg.axes[1]
        twist.angular.z = self.angular_scale * msg.axes[0]
        self.cmd_vel_pub.publish(twist)

        bool = Bool()
        if self.frame_id_old != self.frame_id:
            self.frame_id_old = self.frame_id
            if self.button[2] == 1: # If X
                # print("test")
                if self.bool.data:
                    # self.get_logger().info(f'Open arms', once=True)
                    self.bool.data = False
                else:
                    # self.get_logger().info(f'Close arms', once=True)
                    self.bool.data = True
        self.publisher.publish(self.bool)

def main(args=None):
    rclpy.init(args=args)
    joy_to_cmd_vel = JoyToCmdVel()
    rclpy.spin(joy_to_cmd_vel)
    joy_to_cmd_vel.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
