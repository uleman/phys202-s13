import numpy as np
def pointPotential(x,y,q,posx,posy):
    k=8.987*10**9#Nm^2/c^2
    d=1
    Vxy=(k*q)/(x**2+(y-d)**2)**(1/2.)
    return Vxy
def dipolePotential(x,y,q,d):
    k=8.987*10**9#Nm^2/c^2
    Vxy=(k*q)/(x**2+(y-d)**2)**(1/2.)-(k*q)/(x**2+(y+d)**2)**(1/2.)
    return Vxy
def pointField(x,y,q,Xq,Yq):
    k=8.987*10**9#Nm^2/c^2
    Ex = (k*q*(x-Xq))/((x-Xq)**2+(y-Yq)**2)**(1/2.)
    Ey = (k*q*(y-Yq))/((x-Xq)**2+(y-Yq)**2)**(1/2.)
    return Ex,Ey
"""Added the PointField Equation for the midterm that takes the arguments of """

