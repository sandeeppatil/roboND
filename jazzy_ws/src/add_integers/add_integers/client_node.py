import sys

import rclpy
from rclpy.node import Node
from custom_interfaces.srv import AddTwoInts

class ClientNodeAsync(Node):
  def __init__(self):
    super().__init__('add_integers_client')
    self.client_ = self.create_client(AddTwoInts, 'add_two_ints')
    while not self.client_.wait_for_service(timeout_sec=1.0):
      self.get_logger().info('service not available, waiting again...')

  def send_request(self):
    request = AddTwoInts.Request()
    request.a = int(sys.argv[1])
    request.b = int(sys.argv[2])
    self.future = self.client_.call_async(request)

def main(args=None):
  rclpy.init(args=args)
  client_node = ClientNodeAsync()
  client_node.send_request()
  
  while rclpy.ok():
    rclpy.spin_once(client_node) # also check spin_until_future_complete() and spin()
    if client_node.future.done():
      try:
        response = client_node.future.result()
      except Exception as e:
        client_node.get_logger().info('Service call failed %r' % (e,))
      else:
        client_node.get_logger().info('Result of add_two_ints: %d' % (response.sum))
      break
  client_node.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()