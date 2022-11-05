<h1 align="center"; style="text-align:center;">Laboratory 5: Invers kinematics - Phantom X - ROS</h1>
<p align="center";style="font-size:50px; text-align:center; line-height : 50px;  margin-top : 0; margin-bottom : 0; "> <br> Universidad Nacional de Colombia</p>
<p align="center";style="font-size:50px; text-align:center; line-height : 50px;  margin-top : 0; margin-bottom : 0; "> <br> Robotics</p>
<p align="center";style="font-size:50px; text-align:center; line-height : 40px;  margin-top : 0; margin-bottom : 0; "> <br> Santiago Mariño (samrinoj) - Daniel Pineda (dpinedasi)</p>


<p align="center"; style="font-size:50px; text-align:center; line-height : 30px; margin-top : 0; "> <br>November 4th  2022</p>

## Solution Description

### DHstd parameters

With the help of a caliper, the length of the links, which are found in figure 1, is measured. With these lengths and the angles of the Home position, the DHst table is made.

![Measurements](https://github.com/dpinedasi/Lab4Rob/blob/main/imagenes/LINKS.png)

In the case of L1, two meassurements had to be done as the link has a L shape. Then the Pythagoras theorem was applied in order to find the minimum distance between the two join axes.

![DH parameters](https://github.com/dpinedasi/Lab4Rob/blob/main/imagenes/dhstd.png)

### Invers kinematics

Dado que el robot presenta solo articulaciones cilindricas 5 articulaciones cilindricas, se decide resolver la cinematica inversa geometricamente:

Se tiene el valor de $q_1$ como:

$$
\begin{gather*}
    q_1=\mathrm{atan2}(X_\mathrm{T},Y_\mathrm{T})
\end{gather*}
$$

Para $q_2$ y $q_3$ :

$$
\begin{gather*}
    ctheta3= \frac{xtr^2+ztr^2-l_1^2-l_2^2}{2*l_1*l_2}\\
    \\
    stheta3= \sqrt{1-ctheta3^2}\\
    \\
    q_3=\mathrm{arctan2}((stheta3),ctheta3)\\
    \\
    \alpha=\mathrm{arctan2}(-ztr,xtr)\\
    \\
    \beta=\mathrm{arctan2}(-l_2*sin(\abs{q_3}),l_1+l_2*cos(\abs{q_3}))\\
    \\
    q_2 = \frac{\pi}{2}+\beta+\alpha-\gamma \\
\end{gather*}
$$

Para q4:

$$
\begin{gather*}
    q_4=\phi-q_2-q_3
\end{gather*}
$$

Codigo

```
pose=np.asanyarray(transl(x,y,43) @ trotx(-5,'deg'))

dt=pose[0:3,3] #distancia tcp
#xt=pose[0,3]   #
#yt=pose[1,3]
#zt=pose[2,3]
approach=pose[0:3,2]
theta1=mt.atan2(dt[1],dt[0])
if abs(theta1)>pi/2:
    theta1 = atan2(-dt[1],-dt[0])
w=dt-l[3]*approach
xtr=np.sqrt(w[0]**2+w[1]**2)
ztr=w[2]-l[0]
ctheta3=((xtr**2+ztr**2-l[1]**2-l[2]**2)/(2*l[1]*l[2]))
stheta3=mt.sqrt(1-ctheta3**2)
theta3=atan2((stheta3),ctheta3)
alpha=atan2(-ztr,xtr)
beta=atan2(-l[2]*mt.sin(abs(theta3)),l[1]+l[2]*mt.cos(abs(theta3)))
theta2=alpha+beta+pi/2
phi = atan2(pose[2,2], mt.sqrt(pose[0,2]**2 +pose[1,2]**2)) - pi/2

H10=MTHDH(0,pi/2,l[0],theta1)
H21=MTHDH(l[1],0,0,theta2)
H32=MTHDH(l[2],0,0,theta3)

HT3=np.linalg.inv(H10*H21*H32)*pose

theta4 = atan2(-HT3[0,0],HT3[1,0])


theta4=(phi-theta2-theta3)%pi

if theta4>=pi/2:
    theta4=theta4-pi
elif theta4<=-pi/2:
    theta4=theta4+pi

q=np.array([theta1,-theta2,-theta3,-theta4])
q
```



