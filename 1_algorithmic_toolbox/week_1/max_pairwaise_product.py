# Uses python2
#import time
#n = input()
#a = [int(x) for x in raw_input().split()]
#assert(len(a) == n)

#result = 0
#s = time.time()
#for i in range(0, n):
    #for j in range(i+1, n):
        #if a[i]*a[j] > result:
            #result = a[i]*a[j]
#print "time taken", str(time.time() -s)

#s = time.time()
#a.sort()
#print a[-1] * a[-2]
#print(result)
#print "time taken", str(time.time() -s)


## Finding max1, max2
a = [1,2,3,4,1090,4,49,582, 1090]
max1 = 0
max2 = 0

for i in range(0, len(a)):
    if a[i] > a[max1]:
        max1 = i

for j in range(0, len(a)):
    if (a[j] > a[max2]) and (max1 != j):
        max2 = j



print a[max1], max1
print a[max2], max2



