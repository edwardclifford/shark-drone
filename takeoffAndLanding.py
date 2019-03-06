import roslib; roslib.load_manifest('')
import rospy

from geometry_mesgs.msg import Twist
from std_msgs import Empty

def takeoff():
    pub = rospy.Publisher('bebop/takeoff', Empty, queue_size = 1)
    pub.publish()
    return

def land():
    pub = rospy.Publisher('bebop/land', Empty, queue_size = 1)
    pub.publish()
    return

if __name__ == "__main__":
    rospy.init_node('')
    takeoff()
    # pub = rospy.Publisher('cmd_vel', Twist, queue_size = 1)

    #Set movement here, values excepter are between 1 and -1
    # twist = Twist()
    # twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
    # twist.angular.x = 0; twist.angular.y = 0, twist.angular.z = 0
    # pub.publish(twist)
    land()
