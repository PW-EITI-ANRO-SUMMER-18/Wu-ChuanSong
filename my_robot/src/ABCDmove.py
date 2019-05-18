#!/usr/bin/env python
# license removed for brevity
import roslib; roslib.load_manifest('my_robot')
import rospy
import math
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

def interpolate( p1, p2, f ):
    p1x = p1[0]
    p1y = p1[1]
    p1z = p1[2]

    p2x = p2[0]
    p2y = p2[1]
    p2z = p2[2]

    interpolated_x = p1x*(1.0-f) + p2x*f
    interpolated_y = p1y*(1.0-f) + p2y*f
    interpolated_z = p1z*(1.0-f) + p2z*f

    return (interpolated_x, interpolated_y, interpolated_z)

'''def test():
	print "this is test"
	
	point1 = (0,0,10)
	point2 = (1,10,0)
	variable = interpolate(point1, point2, 0.25)
	
	print variable'''
		
cmd = JointState()

def talker():
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    rospy.init_node('joint_state_publisher1')
    rate = rospy.Rate(10) # 10hz	
    f=0.0
    flag = 0
    i=1
    j=1
    k=1
    l=1
    A=(0.1,0.1,0.0)	
    B=(0.1,0.2,0.2)
    C=(0.2,0.1,0.1)
    D=(0.3,0.0,0.1)
    while not rospy.is_shutdown():
		hello_str = "hello world %s" % rospy.get_time()     
		rospy.loginfo(hello_str)
		v=0.05
		n=1/v
		f=f+v
		if f<=1 and flag==0:
			x,y,z=interpolate( A, B, f )
			i=i+1
			if i==n:
				flag=1
				f=0.0
				l=1
		if f<=1 and flag==1:
			x,y,z=interpolate( B, C, f )
			j=j+1
			if j==n:
				flag=2
				f=0.0
				i=1
		if f<=1 and flag==2:
			x,y,z=interpolate( C, D, f )
			k=k+1
			if k==n:
				flag=3
				f=0.0
				j=1
		if f<=1 and flag==3:
			x,y,z=interpolate( D, A, f )
			l=l+1
			if l==n:
				flag=0
				f=0.0
				k=1
		print(flag)
		print(x,y,z)
		print(i,j,k,l)
		cmd.header=Header()
		cmd.header.stamp=rospy.Time.now()
		cmd.name=['base_to_two','two_to_three','three_to_four']
		cmd.position=[z,x,y]
		cmd.velocity=[]
		cmd.effort=[]
		pub.publish(cmd)
		rate.sleep()
		

			
		
		
		
if __name__ == '__main__':
    try:
		#test()
        talker()
    except rospy.ROSInterruptException:
        pass
