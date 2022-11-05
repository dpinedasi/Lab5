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
        if key == 'Q':
            aux =  [1.4, 1.2,-1.7,-1.4,-1*pi/48]
            key=' '
        elif key == 'H':
            aux =  [1.4,0,0,0,-1*pi/48]
            key=' '
        elif key == 'q':
            #[0,-0,-0,-0,0]
            aux =  [1.57079633, -1.22984052, -1.67692387,  1.42323452,-1*pi/48]
            #aux =  [-0.        ,  -0.78538281,  -1.35377102, 0.04475873,-1*pi/48]
            key=' '
        elif key == 'w':
            aux =  [1.57079633, -1.08613822, -1.44382707,  1.04643542,-1*pi/48]
            key=' '
        elif key == 'e':
            aux =  [1.57079633, -1.08613822, -1.44382707,  1.04643542,-28*pi/48]
            key=' '
        elif key == 'r':
            aux = [1.57079633, -0.79760199, -1.50783917,  0.82191129,-28*pi/48]
            key=' '
        elif key == 't':
            aux = [1.4, -0.69594272, -1.70617862,  0.91859148,-28*pi/48]
            key=' '
        elif key == 'y':
            aux = [1.4, -1.2, -2,  1.8,-28*pi/48]
            key=' '
        elif key == 'u':
            aux = [-1.4, -1.2, -2,  1.8,-28*pi/48]
            key=' '
        elif key == 'i':
            aux = [-1.4, -0.95091113, -1.82220786,  1.28958913,-28*pi/48]
            key=' '  
        elif key == 'o':
            aux =  [-1.4        , -1.5728549 , -0.46368298,  0.55300802,-28*pi/48]
            key=' '      
        elif key == 'p':
            aux =  [1.4        , -1.52699452, -0.507424  ,  0.55088865,-28*pi/48]
            key=' '  
        
        elif key == 'a':
            aux = [ 1.4        , -1.4, -0.507424  ,  0.55088865,-28*pi/48]
            #aux = [ 1.40,  0.2989218 , -2.21066795, -1.14258003,-28*pi/48]
            key=' '
        elif key == 's':
            aux = [  1.28474489, -1.12657504, -1.34343484,  0.98648001,-28*pi/48]
            #aux = [ pi/2, 0.34627169,  -2.22509598,  -1.26276836,-28*pi/48]
            key=' '
        elif key == 'd':#llega a la d
            aux = [ 1.28474489, -1.32805643, -1.22517083,  1.0696974,-28*pi/48]
            key=' '         
        elif key == 'f':#primer trazo D
            aux = [ 1.28070939, -1.28484774, -1.45564131,  1.25695918,-28*pi/48]
            key=' ' 
        elif key == 'g':#segundo trazo D
            aux = [ 1.28700222, -1.22722953, -1.69026628,  1.43396594,-28*pi/48]
            key=' '
        elif key == 'h':
            aux = [ 1.22524075, -1.23283268, -1.66218578,  1.4114886,-28*pi/48]
            key=' '
        elif key == 'j':#
            aux = [ 1.20362249, -1.23837923, -1.63617321,  1.39102258,-28*pi/48]
            key=' '
        elif key == 'k':#
            aux = [ 1.19646271, -1.24990962, -1.58625503,  1.35263478,-28*pi/48]
            key=' '
        elif key == 'K':#
            aux = [ 1.21, -1.24990962, -1.58625503,  1.35263478,-28*pi/48]
            key=' '
        elif key == 'l':#
            aux = [ 1.21, -1.33702948, -1.3301179 ,  1.15,-28*pi/48]
            key=' '
        elif key == 'L':#
            aux = [ 1.23755203, -1.35367333, -1.2793598 ,  1.14950326,-28*pi/48]
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
            aux = point.positions = [-1.57079633, -0.63324398, -0.91517015, -1.50591206,-28*pi/48 ]    
            key=' '     
        elif key == 'zs':
            aux = point.positions = [1.40, -0.92756065, -0.52941735,  -1.54424446,-28*pi/48 ]    
            key=' '
        elif key == 'xs':
            aux = point.positions = [1.40, -0.84369069, -0.67794319, -1.53269231,-28*pi/48 ]   
            key=' '
        elif key == 'cs':
            aux = point.positions = [1.40, -0.77278232, -0.79974364, -1.48180023,-28*pi/48 ]    
            key=' '
        elif key == 'v':
            aux = point.positions = [1.40, -0.70937276, -0.90564262, -1.43931081,-28*pi/48 ]   
            key=' '
        elif key == 'bs':
            aux = point.positions = [1.40, -0.65090103, -1.00067657, -1.40274859,-28*pi/48 ]   
            key=' '
        elif key == 'ns':
            aux = point.positions = [1.40, -0.59591265, -1.08767112, -1.37074242,-28*pi/48 ]   
            key=' '
        elif key == 'ms':
            aux = point.positions = [1.40, -0.54347991, -1.16839571, -1.34245057,-28*pi/48 ]   
            key=' '
        elif key == 'us':
            aux = point.positions = [-0.        , -0.21148479,  0.96232561, -1.40,-28*pi/48 ]   
            key=' '
        elif key == 'hs':
            aux = point.positions = [0, -pi/2, pi/2, pi/4,-28*pi/48 ]    
            key=' '
        elif key == 'm':
            aux = point.positions = [0.78539816, -1.38368349, -1.19231734,  1.09247096,-28*pi/48 ]    
            key=' '
        elif key == 'n':
            aux = point.positions = [0.82900469, -1.52453223, -0.82947176,  0.87047413,-28*pi/48 ]    
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