import numpy as np
import matplotlib.pyplot as plt
import math

alpha = 0.000014
beta = 0.2

def F(x,y) : # y[0] : S y[1] : I  y[2] : R
    return np.array([-alpha*y[1]*y[0],alpha*y[1]*y[0]-beta*y[1],beta*y[1]])

def approx_num3(t0,T,h,y0,Phi):
    t = np.arange(t0,t0+T,h)
    y = np.zeros((3,len(t)))
    y[:,0]=y0
    print()
    for i in range(1,len(t)) :
        print(y)
        #print(Phi(y[-1],h,t[i-1]))
        y[:,i] = y[:,i-1] + h*Phi(y[:,i-1],h,t[i-1])
    return [y[0],y[1],y[2]]

def katta(y,h,t) :
    a = F(t,y)
    b = F(t+(h/2),y+(h/2)*a)
    c = F(t+(h/2),y+(h/2)*b)
    d = F(t+h,y+h*c)
    return (a+2*b+2*c+d)/6


x = np.arange(0,100.5,0.5)
y = approx_num3(0,100.5,0.5,[49995.0,5.0,0.0],katta)[0]
y2 = approx_num3(0,100.5,0.5,[49995.0,5.0,0.0],katta)[1]
y3 = approx_num3(0,100.5,0.5,[49995.0,5.0,0.0],katta)[2]

c_a, = plt.plot(x,y,'b')
c_a2, = plt.plot(x,y2,'g')
c_a3, = plt.plot(x,y3,'black')

c_a.set_label("Sain")
c_a2.set_label("Infecté")
c_a3.set_label("Résistant")

plt.legend()
plt.grid(color="grey",linestyle="--")
plt.show()
