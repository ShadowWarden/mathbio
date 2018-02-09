# mathbio/src
#
# Omkar H. Ramachandran
# omkar.ramachandran@colorado.edu
#
# Python script that plots a cobweb diagram of a given function
#

import numpy as np
import matplotlib.pyplot as plt

def f(x,params):
    return params[0]*x/(1+x)*(x/(x+params[1]))

def draw_cobweb(f,N,x0,params,titlestring):
    """ Draws a cobweb diagram using a very simple algorithm:
        1. Mark points x[i],y[i] that lie on the function for odd i
        2. For even i, set x[i] = y[i-1]
    """
    x = np.zeros(N+1)
    y = np.zeros(N+1)
    # Set initial conditions
    y[0] = x0[1]
    x[0] = x0[0]
    for i in range(1,N,2):
        # Odd i
        x[i] = x[i-1]
        y[i] = f(x[i-1],params)
        # Even i
        x[i+1] = y[i]
        y[i+1] = y[i]

    # Plot the function
    plt.plot(x,y,color='b')
    plt.grid()
    plt.xlabel(r"$x$")
    plt.ylabel(r"$f(x)$")
    plt.title(titlestring)

    X = np.linspace(0,max(x),1000)
    Y = f(X,params)
    plt.plot(X,Y,color='r')

    Yline = X
    plt.plot(X,Yline,'-.')
    plt.draw()

N = 50
Nruns = 1
R0 = np.linspace(2,5,Nruns)
R0 = 10**(R0)
Nmax = -1 + 0.5*np.sqrt(4+4*(R0-1))
x0 = np.array([0.2,0.0])
Sc = (R0*Nmax-Nmax-Nmax**2)/(Nmax+1)
print(Sc)

plt.figure(0)
params = np.array([R0,Sc+1])
draw_cobweb(f,N,x0,params,r"Cobweb diagram for the $S = S_c+1$")
plt.figure(1)
params = np.array([R0,Sc-1])
draw_cobweb(f,N,x0,params,r"Cobweb diagram for the $S < S_c$")


plt.show()
