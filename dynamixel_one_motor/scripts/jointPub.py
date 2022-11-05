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
        state = JointTrajectory()
        state.header.stamp = rospy.Time.now()
        state.joint_names = ["joint_1","joint_2","joint_3","joint_4","joint_5"]
        point = JointTrajectoryPoint()
        if key == 'q':
            #[0,-0,-0,-0,0]
            
            #aux =  [-0.        ,  0.61167893,  1.7029451 , -0.34240198,-1*pi/48]
            #aux =  [-0.        ,  0.76430391,  2.07262907, -0.82980434,-1*pi/48]# segundo agarre
            aux =  [-0,  0.62943155,  1.82743112,  -0.4,-1*pi/48] #primer agarre
            key=' '
        if key == 'a':
            aux = [-0.        ,  0.61167893,  1.7029451 , -0.34240198,-28*pi/48]
            key=' '
        elif key == 's':
            aux = [-0.        ,  0.30210204,  2.02864193, -0.35852191,-28*pi/48]
            key=' '
        elif key == 'S':
            aux = [-0.        , -0.04656087,  2.21432251, -0.19553959,-28*pi/48]
            key=' '
        elif key == 'e':
            aux = [-0.        , -0.25984255,  2.25984791, -0.0277833 ,-28*pi/48]
            key=' '    
        elif key == 'd':
            aux = [ 1.57079633, -0.30161081,  2.56633513,  0.87686833,-28*pi/48]
            #aux = [ pi/2, 0.34627169,  -2.22509598,  -1.26276836,-28*pi/48]
            key=' '
        elif key == 'f':
            aux = [ -pi/2, -0.3624896 , -1.4319315 , -1.34717155,-28*pi/48]
            key=' ' 
        elif key == 'h':
            aux = point.positions = [0, -pi/2, pi/2, pi/4,-27*pi/48 ]    
            key=' '
        elif key == 'j':
            aux = point.positions = [pi/2, -0.98324768, -0.36328059, -1.79506439,-28*pi/48 ]    
            key=' '   
        elif key == 'k':
            aux = point.positions = [-pi/2, -0.97258217, -0.40230609, -1.7667044,-27*pi/48 ]    
            key=' '     
        elif key == 'z':
            aux = point.positions = [pi/2, -0.88277256, -0.5260437 , -1.7327764,-28*pi/48 ]    
            key=' '
        elif key == 'x':
            aux = point.positions = [pi/2, -0.66376703, -0.91622168, -1.56160395,-27*pi/48 ]   
            key=' '
        elif key == 'c':
            aux = point.positions = [pi/2, -0.72652491, -0.81357392, -1.60149382,-27*pi/48 ]    
            key=' '
        elif key == 'v':
            aux = point.positions = [0,2.95005504e-01,  1.93296087e-01,  1.08249474e+00,-27*pi/48 ]   
            key=' '
        elif key == 'r':
            aux = point.positions = [pi/2,0,0,0,-27*pi/48 ]   
            key=' '
        elif key == 't':
            aux = point.positions = [0,pi/2,0,0,-27*pi/48 ]   
            key=' '
        elif key == 'y':
            aux = point.positions = [-0.        ,  0.56591898,  1.71936575,  pi-2.95070303,-1*pi/48 ]   
            key=' '
        elif key == 'u':
            aux = point.positions = [-0.        , -0.21148479,  0.96232561, -1.57079633,-27*pi/48 ]   
            key=' '
        point.positions = aux   
        point.time_from_start = rospy.Duration(0.5)
        state.points.append(point)
        pub.publish(state)
        print('published command')
        rospy.sleep(1)

if __name__ == '__main__':
    try:
        joint_publisher()
    except rospy.ROSInterruptException:
        pass