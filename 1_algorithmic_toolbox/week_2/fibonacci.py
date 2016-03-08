# finding fibonacci
# 0 1 1 2 3 5 8 13 21
import time
import random

def fibonacci_simple(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_simple(n-1) + fibonacci_simple(n-2)

# to test fibonacci_simple method
#print fibonacci_simple(0) # 0
#print fibonacci_simple(1) # 1
#print fibonacci_simple(2) # 1
#print fibonacci_simple(6) # 8
#print fibonacci_simple(8) # 21


# calculating time
run_times = []
for i in range(1, 1001):
    n = random.randint(1,30)
    s = time.time()
    fibonacci_simple(n)
    run_times.append(time.time() - s)

#print "Average for 1000 runs for fibonacci_simple is: %s" % str(sum(run_times)/1000)
time_calc = (sum(run_times)/1000)
print "Average time for 1000 run after normalizing by multiplying with 1000000 is: %s" % str(time_calc * 1000000)

def fibonacci_efficient(n):
    fibs = [0,1]

    if n == 0 or n == 1:
        return fibs[n]
    for i in range(2, n+1):
        fibs.append(fibs[i-1] + fibs[i-2])

    return fibs[n]

# to test fibonacci_simple method
#print fibonacci_efficient(0) # 0
#print fibonacci_efficient(1) # 1
#print fibonacci_efficient(2) # 1
#print fibonacci_efficient(6) # 8
#print fibonacci_efficient(8) # 21

run_times = []
for i in range(1, 1001):
    n = random.randint(1,30)
    s = time.time()
    fibonacci_efficient(n)
    run_times.append(time.time() - s)

#print "Average for 1000 runs for fibonacci_efficient is: %s" % str(sum(run_times)/1000)
time_calc = (sum(run_times)/1000)
print "Average time for 1000 run after normalizing by multiplying with 1000000 is: %s" % str(time_calc * 1000000)
