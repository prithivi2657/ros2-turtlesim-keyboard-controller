import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys
import termios
import tty
import select


class TurtleController(Node):

    def __init__(self):
        super().__init__('turtle_controller')

        self.publisher = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )

        self.timer = self.create_timer(
            0.05,
            self.control_turtle
        )

        self.linear_speed = 0.0
        self.angular_speed = 0.0

        self.get_logger().info('Turtle Keyboard Controller Started')
        self.get_logger().info("Press 'A' for forward")
        self.get_logger().info("Press 'R' for continuous rotation")
        self.get_logger().info("Press 'S' to stop")
        self.get_logger().info("Press 'Q' to quit")

        self.old_settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())

    def get_key(self):
        key = None

        if select.select([sys.stdin], [], [], 0)[0]:
            key = sys.stdin.read(1)

        return key

    def control_turtle(self):
        key = self.get_key()

        if key:
            key = key.lower()

            if key == 'a':
                self.linear_speed = 4.0
                self.angular_speed = 0.0

            elif key == 'r':
                self.linear_speed = 0.0
                self.angular_speed = 4.0

            elif key == 's':
                self.linear_speed = 0.0
                self.angular_speed = 0.0

            elif key == 'q':
                self.linear_speed = 0.0
                self.angular_speed = 0.0
                return

        msg = Twist()
        msg.linear.x = self.linear_speed
        msg.angular.z = self.angular_speed

        if rclpy.ok():
            self.publisher.publish(msg)

    def stop_turtle(self):
        if rclpy.ok():
            msg = Twist()
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.publisher.publish(msg)

    def destroy_node(self):
        if rclpy.ok():
            self.stop_turtle()

        termios.tcsetattr(
            sys.stdin,
            termios.TCSADRAIN,
            self.old_settings
        )

        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)

    node = TurtleController()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
       
