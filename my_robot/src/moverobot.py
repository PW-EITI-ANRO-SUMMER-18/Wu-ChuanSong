#!/usr/bin/env python
# license removed for brevity
import roslib; roslib.load_manifest('my_robot')
import rospy
import math
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

cmd = JointState()
def talker():
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    rospy.init_node('joint_state_publisher1')
    rate = rospy.Rate(10) # 10hz
    r=0.1
    x=0
    y=0
    a=0
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        a=a+0.05
        x=r*math.cos(a)
        y=r*math.sin(a)
        rospy.loginfo(hello_str)
        cmd.header=Header()
        cmd.header.stamp=rospy.Time.now()
        cmd.name=['base_to_two','two_to_three','three_to_four']
        cmd.position=[0,x,y]
        cmd.velocity=[]
        cmd.effort=[]
        
        pub.publish(cmd)
        
        
	rate.sleep()
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
