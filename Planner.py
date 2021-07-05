import rospy
from std_msgs.msg import obstacles

def talker():
  pub=rospy.Publisher('path',obstacles)
  rospy.init_node('talker')
  rate=rospy.Rate(2)
  while not rospy.is_shutdown():
    pub.publish()
    rate.sleep()
