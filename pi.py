
#from math import *

#digits = raw_input('Enter number of digits to round PI to: ')
#print ('{0:.%df}' % min(1000, int(digits))).format(4 * (4 * atan(1.0/5.0) - atan(1.0/239.0)))

#Better way -> own algorithm
position = raw_input('Enter number of digits to round PI to: ')
i = int(position)

def pi():
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    for j in range(i):
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = 10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x
        else:
            q, r, t, k, m, x = q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2


digits = pi()
pi_list = []
array = []

for i in pi():
    array.append(str(i))

array = array[:1] + ['.'] + array[1:]
big_string = "".join(array)
print "Here is fucking pi!:\n %s" % big_string 