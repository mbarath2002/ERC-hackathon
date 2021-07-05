import rospy
from std_msgs.msg import obstacles
def callback():
  print msg.data
  rospy.init_node('receiver')
  sub=rospy.Subscriber('path',obstacles,callback)
  rospy.spin()
  
