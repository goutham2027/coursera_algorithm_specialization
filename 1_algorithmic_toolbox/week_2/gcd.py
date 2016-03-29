import random
import time
from utils import print_normalized_average_runtime

def gcd_naive(a,b):
    gcd = 1
    for i in range(2,min(a,b)):
        if a%i == 0 and b%i == 0:
            gcd = i
    return gcd

# to test gcd_naive
#print "Testing gcd_naive:"
#print gcd_naive(36,24) #12
#print gcd_naive(357,234) # 3
#print gcd_naive(3918848, 1653264) # 61232

run_times = []
for i in range(1,1001):
    randint_1 = random.randint(10,10000)
    randint_2 = random.randint(10,10000)
    s = time.time()
    gcd_naive(randint_1, randint_2)
    run_times.append(time.time() - s)

print_normalized_average_runtime(run_times)
#time_calc = (sum(run_times)/1000)
#print "Average time for 1000 run after normalizing by multiplying with 1000000 is: %s" % str(time_calc * 1000000)

def gcd_efficient(a,b):
    if b == 0:
        return a
    else:
        return gcd_efficient(b, a%b)

# to test gcd_efficient
#print "Testing gcd_efficient:"
#print gcd_efficient(36,24) #12
#print gcd_efficient(357,234) # 3
#print gcd_efficient(3918848, 1653264) # 61232

run_times = []
for i in range(1,1001):
    randint_1 = random.randint(10,10000)
    randint_2 = random.randint(10,10000)
    s = time.time()
    gcd_efficient(randint_1, randint_2)
    run_times.append(time.time() - s)

print_normalized_average_runtime(run_times)
