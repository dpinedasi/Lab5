import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from math import pi
from getkey import getkey, keys

def joint_publisher():
    pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=0)
    rospy.init_node('joint_publisher', anonymous=False)
    aux=[0,0,0,0,0]
    while not rospy.is_shutdown():
        key=input()
        #if KeyboardInterrupt:
        #    key=getkey()
        if key=='a':
            #home
            state = JointTrajectory()
            state.header.stamp = rospy.Time.now()
            state.joint_names = ["joint_1","joint_2","joint_3","joint_4","joint_5"]
            point = JointTrajectoryPoint() 
            aux=[0, -pi/2, pi/2, pi/4,-13*pi/24 ]
            point.positions = aux   
            point.time_from_start = rospy.Duration(0.5)
            state.points.append(point)
            pub.publish(state)
            print('published command')
            rospy.sleep(5)
            #approach
            state = JointTrajectory()
            state.header.stamp = rospy.Time.now()
            state.joint_names = ["joint_1","joint_2","joint_3","joint_4","joint_5"]
            point = JointTrajectoryPoint() 
            aux=[-0,0.62943155,1.82743112,-0.4,-1*pi/24]
            point.positions = aux   
            point.time_from_start = rospy.Duration(0.5)
            state.points.append(point)
            pub.publish(state)
            print('published command')
            rospy.sleep(5)
            #pick up
            state = JointTrajectory()
            state.header.stamp = rospy.Time.now()
            state.joint_names = ["joint_1","joint_2","joint_3","joint_4","joint_5"]
            point = JointTrajectoryPoint() 
            aux=[-0,0.62943155,1.82743112,-0.4,-13*pi/24]
            point.positions = aux   
            point.time_from_start = rospy.Duration(0.5)
            state.points.append(point)
            pub.publish(state)
            print('published command')
            rospy.sleep(5)
            #retire
            state = JointTrajectory()
            state.header.stamp = rospy.Time.now()
            state.joint_names = ["joint_1","joint_2","joint_3","joint_4","joint_5"]
            point = JointTrajectoryPoint() 
            aux=[-0,-0.40624939,2.28416366,0.3282134,-13*pi/24]
            point.positions = aux   
            point.time_from_start = rospy.Duration(0.5)
            state.points.append(point)
            pub.publish(state)
            print('published command')
            rospy.sleep(5)
            #home
            state = JointTrajectory()
            state.header.stamp = rospy.Time.now()
            state.joint_names = ["joint_1","joint_2","joint_3","joint_4","joint_5"]
            point = JointTrajectoryPoint() 
            aux=[0, -pi/2, pi/2, pi/4,-13*pi/24 ]
            point.positions = aux   
            point.time_from_start = rospy.Duration(0.5)
            state.points.append(point)
            pub.publish(state)
            print('published command')
            rospy.sleep(5)


if __name__ == '__main__':
    try:
        joint_publisher()
    except rospy.ROSInterruptException:
        pass