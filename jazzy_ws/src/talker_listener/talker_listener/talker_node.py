import rclpy # Import the ROS client library for ROS 2

from rclpy.node import Node
from std_msgs.msg import String

class TalkerNode(Node):

  # Constructor
  def __init__(self):
    #Initialize the base class
    super().__init__('talker_node')

    # Create a publisher
    self.publisher_ = self.create_publisher(String, 'topic', 10)

    # Create a timer
    timer_period = 0.5

    self.timer = self.create_timer(timer_period, self.timer_callback)
    self.counter = 0

    def timer_callback(self):
      msg = String()
      msg.data = 'Hello World! {self.counter}'
      self.publisher_.publish(msg)
      self.counter += 1
      self.get_logger().info('Publishing: "{msg.data}"')


def main(args=None):
  # Initialize the ROS client library
  rclpy.init(args=args)

  # Create a node
  talkerNode = TalkerNode()

  # Use the Node
  rclpy.spin(talkerNode)

  # Destroy the node
  talkerNode.destroy_node()

  # Shutdown the ROS client library
  rclpy.shutdown()


if __name__ == '__main__':
  main()