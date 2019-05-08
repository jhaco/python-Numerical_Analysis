import matplotlib.pyplot as plt
import numpy as np

x  = np.linspace(0, 1, num=513)
f  = np.sin(2*np.pi*x)
g  = np.abs(x-0.5)

def Y(n,f):
    y = []
    for x in range(0, 512, np.int(512/n)):
        y.append(f[x])
    y.append(f[512])
    return np.array(y)

def Lag(n, x, f):
    a = np.linspace(0, 1, num=n+1)
    b = Y(n,f)
    c = []

    for i in range(0, 513):
        sum = 0
        for j in range(0, len(a)):
            m = 1
            n = 1
            for k in range(0, len(a)):
                if k != j:
                    m = m*(x[int(i)] - a[int(k)])
                    n = n*(a[int(j)] - a[int(k)])
            sum = sum + b[int(j)]*(m/n)
        c.append(sum)

    return np.array(c)


#===============================================================================
fig, ax = plt.subplots()
print('1 - f(x), L4(x), L8(x)')
print('2 - f(x), L16(x)')
print('3 - g(x), L4(x), L8(x)')
print('4 - g(x), L16(x)')
s = int(input('Enter an option: '))
#===============================================================================
if s==1:
    ax.plot(x, f,               color='black',  label='f(x)')
    ax.plot(x, Lag(4, x, f),    color='blue',   label='L4(x)')
    ax.plot(x, Lag(8, x, f),    color='red',    label='L8(x)')
if s==2:
    ax.plot(x, f,               color='black',  label='f(x)')
    ax.plot(x, Lag(16, x, f),   color='blue',   label='L16(x)')
if s==3:
    ax.plot(x, g,               color='black',  label='g(x)')
    ax.plot(x, Lag(4, x, g),    color='blue',   label='L4(x)')
    ax.plot(x, Lag(8, x, g),    color='red',    label='L8(x)')
if s==4:
    ax.plot(x, g,               color='black',  label='g(x)')
    ax.plot(x, Lag(16, x, g),   color='blue',   label='L16(x)')

plt.ylim(-1, 1)
plt.xlim(0, 1)
ax.set(xlabel='x', ylabel='y', title='Lagrange')
ax.grid()
ax.legend()
fig.savefig("test.png")
print('Successful')
plt.show()
