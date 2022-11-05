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
        if key == 1:
            aux = [0,  0,  0, 0,-28*pi/48]
            key=' '
        elif key == 'q':
            #[0,-0,-0,-0,0]
            aux =  [0.        , -0.88592585, -0.92771326, -0.10622307,-1*pi/48] #primer agarre
            #aux =  [-0.        ,  -0.78538281,  -1.35377102, 0.04475873,-1*pi/48]
            key=' '
        elif key == 'w':
            aux = [0.        , -0.88592585, -0.92771326, -0.10622307,-28*pi/48]
            key=' '
        elif key == 'e':
            aux = [0.        , -0.51794864, -1.49461962,  0.09270608,-28*pi/48]
            key=' '
        elif key == 'r':
            aux = [0.        , -0.42190553, -1.58596727,  0.08801062,-28*pi/48]
            key=' '
        elif key == 't':
            aux = [0.        ,  0.10482396, -2.09816561,  0.07347948,-28*pi/48]
            key=' '    
        elif key == 'a':
            aux = [ pi/2,  0.18277333, -2.09227712, -1.23208887,-28*pi/48]
            #aux = [ 1.40,  0.2989218 , -2.21066795, -1.14258003,-28*pi/48]
           
            key=' '
        elif key == 's':
            aux = [ -pi/2,  0.2989218 , -2.21066795, -1.14258003,-28*pi/48]
            #aux = [ pi/2, 0.34627169,  -2.22509598,  -1.26276836,-28*pi/48]
            key=' '
        elif key == 'd':
            aux = [ -pi/2, -1.04215294, -0.31883305,  -1.44825246,-28*pi/48]
            key=' '         
        elif key == 'f':
            aux = [ 1.40, -1.05686548, -0.27167492,  -1.41580687,-28*pi/48]
            key=' ' 

        elif key == 'z': #provisional para pruebas de profundidad (acercamiento a F)
            aux = [ 1.40, -0.800345757, -0.22320611,  -1.45393014,-28*pi/48]
            key=' '
        elif key == 'x': #provisional para pruebas de profundidad (acercamiento a F)
            aux = [ 1.57079633, -0.84962226, -0.62005637,  -1.55694509,-28*pi/48]
            key=' '       
        
        elif key == 'c':
            aux = point.positions = [1.57079633, -0.59099374, -1.04773986, -1.41559259,-28*pi/48 ]    
            key=' '   
        elif key == 'v':
            aux = point.positions = [-1.57079633, -0.63324398, -0.91517015, -1.50591206,-27*pi/48 ]    
            key=' '     
        elif key == 'zs':
            aux = point.positions = [1.40, -0.92756065, -0.52941735,  -1.54424446,-28*pi/48 ]    
            key=' '
        elif key == 'xs':
            aux = point.positions = [1.40, -0.84369069, -0.67794319, -1.53269231,-27*pi/48 ]   
            key=' '
        elif key == 'cs':
            aux = point.positions = [1.40, -0.77278232, -0.79974364, -1.48180023,-27*pi/48 ]    
            key=' '
        elif key == 'v':
            aux = point.positions = [1.40, -0.70937276, -0.90564262, -1.43931081,-27*pi/48 ]   
            key=' '
        elif key == 'bs':
            aux = point.positions = [1.40, -0.65090103, -1.00067657, -1.40274859,-27*pi/48 ]   
            key=' '
        elif key == 'ns':
            aux = point.positions = [1.40, -0.59591265, -1.08767112, -1.37074242,-27*pi/48 ]   
            key=' '
        elif key == 'ms':
            aux = point.positions = [1.40, -0.54347991, -1.16839571, -1.34245057,-27*pi/48 ]   
            key=' '
        elif key == 'us':
            aux = point.positions = [-0.        , -0.21148479,  0.96232561, -1.40,-27*pi/48 ]   
            key=' '
        elif key == 'hs':
            aux = point.positions = [0, -pi/2, pi/2, pi/4,-27*pi/48 ]    
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