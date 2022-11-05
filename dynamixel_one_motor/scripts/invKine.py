import numpy as np
import math as mt
from math import pi
from math import atan2

def invKine(l,pose):
    try:
        dt=pose[0:3,3] #distancia tcp
        approach=pose[0:3,2]
        theta1=mt.atan2(dt[1],dt[0])
        if abs(theta1)>pi/2:
            theta1 = atan2(-dt[1],-dt[0])
        w=dt-l[3]*approach
        xtr=np.sqrt(w[0]**2+w[1]**2)
        ztr=w[2]-l[0]
        theta3=mt.acos((xtr**2+ztr**2-l[1]**2-l[2]**2)/(2*l[1]*l[2]))
        alpha=atan2(-ztr,xtr)
        beta=atan2(-l[2]*mt.sin(abs(theta3)),l[1]+l[2]*mt.cos(abs(theta3)))
        theta2=alpha+beta+pi/2
        phi = atan2(pose[2,2], mt.sqrt(pose[0,2]**2 +pose[1,2]**2)) - pi/2
        theta4=(phi-theta2-theta3)%pi
        q=np.array([theta1,theta2,theta3,theta4])
        return q
    except ValueError:
        print("That position can't be reached with this configuration. Try another movement or configuration")