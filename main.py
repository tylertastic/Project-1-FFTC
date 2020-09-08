'''
Notes:

*** Working! ***

plt.scatter(x, f_ma(x,m), c='green')  <-- puts points at end of each interval defined on line 22
'''

import numpy as np
import matplotlib.pyplot as plt
import math

#Input value vector:
#(a, x0) where a is the parameter and x0 the initial value
#in f_a(x) = ax(1-x) where f: Reals -> Reals

### Settings
print("The function being used is f_a(x) = ax(1-x)")
print("-------------------------------------------")
a = float(input("Enter parameter a: ")) # this should be between 0 and 4 unless axes are changed
x0 = float(input("Enter initial value x0: ")) # this should be between 0 and 1
imax = int(input("Enter the number of iterations: ")) # Any integer -- number of iterations in the sequence, i.e. we want xn where n = imax
m = int(input("Enter m for the mth iterate of f_a: ")) # Any integer, the number of times to iterate f_a (i.e., f_a^(m))

# left = 30 # may not be needed
# w = 300   # number of plotting intervals

### Draw Bisector and Function
plt.axis([0, 1, 0, 1])
x = np.linspace(0, 1, 300)
def f_ma(x_vec, m):  # Recursively defines mth iterate of function f
    if m == 1:
        return a*x_vec*(1-x_vec)
    else:
        return f_ma(f_ma(x_vec, m-1), 1)

plt.plot(x, x, 'b')
plt.plot(x, f_ma(x, m), 'r')
plt.plot([x0, x0], [0, x0], 'g') # initial vertical line from (x0,0) to (x0,x0)

### Start iteration at x0
xn = x0

# Draw vertical and horizontal lines
for i in range(1,imax+1):
    plt.plot([xn, xn], [xn, f_ma(xn, m)], 'g') #vertical from (xi, xi) to (xi, f(xi))
    plt.plot([xn, f_ma(xn, m)], [f_ma(xn, m), f_ma(xn, m)], 'g') #horizontal from (xi, f(xi)) to (f(xi), f(xi))
    xn = f_ma(xn, m)
    x+=1

plt.show()





