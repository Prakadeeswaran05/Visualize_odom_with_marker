#!/usr/bin/env python
#!coding=utf-8
import rospy
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point
from nav_msgs.msg import Odometry
import sys

class odom_viz:



	def __init__(self):
		
		self.odom_sub = rospy.Subscriber('/odom',Odometry,self.callback)
		self.marker_pub=rospy.Publisher("marker_test", Marker, queue_size=10)
		self.count=0
		self.marker=Marker()

	def callback(self,msg):
		self.marker.header.frame_id = "map"
		self.marker.header.stamp = rospy.Time.now()
				
		self.marker.id = 0
		self.marker.action = Marker.ADD
		self.marker.lifetime = rospy.Duration()
		self.marker.type = Marker.POINTS
		self.marker.color.r = 1.0
		self.marker.color.g = 0.0
		self.marker.color.b = 0.0
		self.marker.color.a = 1.0

		self.marker.scale.x = 0.01
		self.marker.scale.y = 0.1
		self.marker.scale.z = 0.1 
		if self.count==0:
			self.marker.points=[]
			self.init_point=Point()
			self.init_point.x = msg.pose.pose.position.x
			self.init_point.y = msg.pose.pose.position.y
			self.init_point.z = msg.pose.pose.position.z
			self.marker.points.append(self.init_point) 
			self.marker_pub.publish(self.marker)
		else:
			self.marker_point=Point()
			self.marker_point.x = msg.pose.pose.position.x
			self.marker_point.y = msg.pose.pose.position.y
			self.marker_point.z = msg.pose.pose.position.z
			self.marker.points.append(self.marker_point)
			self.marker_pub.publish(self.marker)
  
		self.count+=1

def main(args):
	od = odom_viz()
	rospy.init_node('odom_viz', anonymous=True)
	try:
		rospy.spin()
	except rospy.ROSInterruptException:
		pass

if __name__ == '__main__':
	main(sys.argv)

    


