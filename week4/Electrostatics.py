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
