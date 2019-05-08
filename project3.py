import numpy as np

exact = np.float32(1.416146836547142)
f = lambda x: np.sin(x)

#Midpoint Rule
#Points: 0.125, 0.375, 0.625, 0.875, 1.125, 1.375, 1.625, 1.875
def Midpoint(n, f):
    total = np.float32(0)
    delta = np.float32(2/n)
    for x in range(0, n):
        total += delta*f(delta*x+0.125)
    return total

#Trapezoidal Rule
#Points: 0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2
def Trapezoidal(n, f):
    total = np.float32(0)
    delta = np.float32(2/n)
    for x in range(0, n):
        total += (delta/2)*(f(x*delta) + f((x+1)*delta))
    return total

#Simpson's Rule
#Points: 0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2
def Simpson(n, f):
    total = np.float32(0)
    delta = np.float32(2/n)
    for x in range(0, n, 2):
        total += (delta/3)*(f(x*delta) + 4*f((x+1)*delta) + f((x+2)*delta))
    return total

#Gaussian Quadrature (3, 4, 5 points) (need change of variable; used table)
def GQuad3(f):
    total = np.float32(0)
    total += (8/9)*f(1) + \
             (5/9)*(f(1-np.sqrt(3/5)) + \
                    f(1+np.sqrt(3/5)))
    return total

def GQuad4(f):
    total = np.float32(0)
    total += ((18+np.sqrt(30))/36)*(f(1-np.sqrt((3/7)-(2/7)*np.sqrt(6/5))) + \
                                    f(1+np.sqrt((3/7)-(2/7)*np.sqrt(6/5)))) + \
             ((18-np.sqrt(30))/36)*(f(1-np.sqrt((3/7)+(2/7)*np.sqrt(6/5))) + \
                                    f(1+np.sqrt((3/7)+(2/7)*np.sqrt(6/5))))
    return total

def GQuad5(f):
    total = np.float32(0)
    total += (128/225)*f(1) + \
             ((322+13*np.sqrt(70))/900)*(f(1-(1/3)*np.sqrt(5-2*np.sqrt(10/7))) + \
                                         f(1+(1/3)*np.sqrt(5-2*np.sqrt(10/7)))) + \
             ((322-13*np.sqrt(70))/900)*(f(1-(1/3)*np.sqrt(5+2*np.sqrt(10/7))) + \
                                         f(1+(1/3)*np.sqrt(5+2*np.sqrt(10/7))))
    return total
print('Integration Method')
print('Midpoint:    ' + str(Midpoint(8,f)))
print('Trapezoidal: ' + str(Trapezoidal(8,f)))
print('Simpsons:    ' + str(Simpson(8,f)))
print('GQuad3:      ' + str(GQuad3(f)))
print('GQuad4:      ' + str(GQuad4(f)))
print('GQuad5:      ' + str(GQuad5(f)))
print('')
print('Corresponding Relative Errors')
print('M : ' + str(np.abs(exact - Midpoint(8,f))))
print('T : ' + str(np.abs(exact - Trapezoidal(8,f))))
print('S : ' + str(np.abs(exact - Simpson(8,f))))
print('G3: ' + str(np.abs(exact - GQuad3(f))))
print('G4: ' + str(np.abs(exact - GQuad4(f))))
print('G5: ' + str(np.abs(exact - GQuad5(f))))
