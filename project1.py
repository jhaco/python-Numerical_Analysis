import math
import numpy

s = int(input('Enter a value for s: '))
n = int(input('Enter a value for n: '))
N = int(math.pow(10,n))
print('Input:\n  s = ' + str(s) + '\n  n = ' + str(n) + '\n  N = ' + str(N))

fsum = numpy.float32(0)
bsum = numpy.float32(0)
for x in range(1, N+1):
    fsum += 1/(math.pow(x,s))
    bsum += 1/(math.pow((N+1-x),s))

fdif = numpy.float32(0)
bdif = numpy.float32(0)
if s == 2:
    fdif = abs(1.6449340668482264-fsum)
    bdif = abs(1.6449340668482264-bsum)

if s == 3:
    fdif = abs(1.20205690315959-fsum)
    bdif = abs(1.20205690315959-bsum)

print('\nForward sum:   ' + str(fsum))
print('\nBackward sum:  ' + str(bsum))
print('\nForward diff:  ' + str(fdif))
print('\nBackward diff: ' + str(bdif))
print('\nRatio:         ' + str((min(fdif,bdif)/max(fdif,bdif))*100) + '%')
