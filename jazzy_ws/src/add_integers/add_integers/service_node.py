import rclpy
from rclpy.node import Node
from custom_interfaces.srv import AddTwoInts

class ServiceNode(Node):
  def __init__(self):
    super().__init__('add_integers_service')
    self.service_ = self.create_service(
      AddTwoInts, # service type (data structure)
      'add_two_ints', # service name
      self.add_two_ints_callback # callback function
    )

  def add_two_ints_callback(self, request, response):
    response.sum = request.a + request.b
    self.get_logger().info('Incoming request a: %d b: %d' % (request.a, request.b))
    self.get_logger().info('Sending response: %d' % response.sum)
    return response


def main(args=None):
  rclpy.init(args=args)

  # Create the node
  service_node = ServiceNode()

  # spin the node so the service can be called
  rclpy.spin(service_node)

  # Destroy the node explicitly
  service_node.destroy_node()

  # Shutdown the ROS client library for Python
  rclpy.shutdown()
   

if __name__ == '__main__':
  main()