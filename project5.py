import numpy as np

#MACHINE PROBLEM 5: Due April 18, 2019
#Solve Problem 27 from section 6.6: page 413 (8th edition), page 428 (9th edition).
#That means the following:
#(a) Write a code for the Crout Factorization Algorithm 6.7 for any given three diagonal matrix A, see the notation from the problem.
#(b) Find the solution of Ax=f using your code and print out your results for the following two cases
#Case 1. n=16,  a_i=4,      b_i=1,  c_i=1,   f_i=1,     i=1,2,...,16
#Case 2. n=16,  a_i=2014,   b_i=4,  c_i=10,  f_i=14,    i=1,2,...,16
#The INPUT of the code for your Crout Factorization Algorithm 6.7 should be a, b, c and f (the right-hand side vector)

#GOAL: find x of Ax=f by Lz=f and Ux=z

def popA(n, a, b, c):                                           #populates A with required diagonals
    A = np.zeros(shape=(n,n))
    for i in range (0,n):
        A[i,i]          = a
        if i != 0:
            A[i,i-1]    = b
        if i != n-1:
            A[i,i+1]    = c
    return A

def popU(n):                                                    #populates U with a 1-diagonal
    U = np.zeros(shape=(n,n))
    for i in range (0,n):
        U[i,i]          = 1
    return U

def Crout(n, a, b, c, f):
    A = popA(n, a, b, c)                                        #initialize A
    L = np.zeros(shape=(n,n))                                   #initializes L
    U = popU(n)                                                 #initializes U
    z = np.zeros(shape=n)                                       #initializes z in Lz = f
    x = np.zeros(shape=n)                                       #initializes x in Ux = z

    #========================
    L[0,0]  = A[0,0]                                            #Crout Factorization Algorithm 6.7 rewritten
    U[0,1]  = A[0,1]/L[0,0]                                     #adjustments to range
    z[0]    = f[0]/L[0,0]

    for i in range (1,n-1):                                     #populates L and U and z
        L[i,i-1]    = A[i,i-1]
        L[i,i]      = A[i,i] - L[i,i-1]*U[i-1,i]
        U[i,i+1]    = A[i,i+1]/L[i,i]
        z[i]        = (f[i] - L[i,i-1]*z[i-1])/L[i,i]
    #========================
    L[n-1,n-2]  = A[n-1,n-2]                                    #last line of L and z
    L[n-1,n-1]  = A[n-1,n-1] - L[n-1,n-2]*U[n-2,n-1]
    z[n-1]      = (f[n-1] - L[n-1,n-2]*z[n-2])/L[n-1,n-1]
    #========================
    x[n-1] = z[n-1]                                             #populates x
    for i in range (n-2, -1, -1):
        x[i]    = z[i] - U[i,i+1]*x[i+1]

    return x

print("Case 1")
print(Crout(16, 4, 1, 1, [1]*16))
print("Case 2")
print(Crout(16, 2014, 4, 10, [14]*16))
#print(Crout(4, 2, -1, -1, [1,0,0,1]))
