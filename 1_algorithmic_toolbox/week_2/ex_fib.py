## Problem Statement
'''
Given an integer n, find the last digit of the nth Fibonacci number
(Fn mod 10)
Constraints: 0<= n<= 10^7
Output: Last digit of Fn
'''

'''
Even fibonacci_efficient turns out slow when we compute for
big number, so instead we have to store last digit.
'''
fibs = [0,1]

def fibonacci_last_digit(n):

    if n == 0 or n == 1:
        return fibs[n]

    if len(fibs) - 1 >= n:
        return fibs[n]

    for i in range(2,n+1):
        fibs.append((fibs[i-1] + fibs[i-2]) % 10)

    return fibs[n]

import time
import random

run_times = []
for i in range(1,26):
    n = random.randint(1,10000000)
    print "%s - %s" % (str(i), str(n))
    s = time.time()
    fibonacci_last_digit(n)
    run_times.append(time.time() - s)

time_calc = (sum(run_times)/25)
print "Average time for 25 run after normalizing by multiplying with 1000000 is: %s" % str(time_calc)

