import numpy as np

#y'=y-4*t*t + 1, y(0)=1.0, and t in the interval [0,1]
#choose h = 0.05

def Euler(f, a, b, h, yn):          #Euler's Method
    w1 = w2 = yn
    n  = int(b/h)
    for i in range (a, n):
        t  = i*h
        w1 = w2
        w2 = w1 + h*f(t,w1)
    return w2

def ModEuler(f, a, b, h, yn):       #Modified Euler's Method
    w1 = w2 = yn
    n  = int(b/h)
    for i in range (a, n):
        t  = i*h
        w1 = w2
        w2 = w1 + (h/2)*(f(t,w1) + f((i+1)*h, w1+h*f(t,w1)))
    return w2

def RK4(f, a, b, h, yn):            #Runge-Kutta 4 Method
    w1 = w2 = yn
    n = int(b/h)
    for i in range (a, n):
        t = i*h
        w1 = w2
        k1 = f(t,w1)*h
        k2 = f(t + h/2, w1 + k1/2)*h
        k3 = f(t + h/2, w1 + k2/2)*h
        k4 = f(t + h, w1 + k3)*h
        w2 = w1 + (k1 + 2*(k2 + k3) + k4)/6
    return w2

#===============================================================================

f   = lambda t,y: y - 4*t*t + 1
yn  = 1.0
a   = 0
b   = 1
h   = 0.05
g   = lambda t: 4*t*t + 8*t + 7 - 6*np.exp(t)       #solved by hand; attached work

n = int(b/h)
print("")
print("t".ljust(7) + "y(t)".ljust(25) + "Euler Abs Error".ljust(25) + "Mod. Euler Abs Error".ljust(25) + "RK4 Abs Error".ljust(25))
for i in range (a, n):
    t = i*h
    p1 = str(round(t,2))                                        #t-value
    p2 = str(g(t))                                              #solved IVP equation
    p3 = str(abs(g(t) - Euler(f, a, t, h, yn)))                 #|p2 - Euler's method|
    p4 = str(abs(g(t) - ModEuler(f, a, t, h, yn)))              #|p2 - Modified Euler's method|
    p5 = str(abs(g(t) - RK4(f, a, t, h, yn)))                   #|p2 - Runge-Kutta 4 method|
    print(p1.ljust(7) + p2.ljust(25) + p3.ljust(25) + p4.ljust(25) + p5.ljust(25))
