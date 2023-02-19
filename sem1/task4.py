"""Is it possible to break off k slices from a chocolate bar of size n × m,
 if we only can make one break in a straight line between the slices
 (to break a chocolate bar into two rectangles)"""

n = int(input("Enter n: "))
m = int(input("Enter m: "))
k = int(input("Enter k: "))
if (k % n) == 0:
    if k // n < m:
        print("yes")
    else:
        print("no")
elif (k % m) == 0:
    if k // m < n:
        print("yes")
    else:
        print("no")
else:
    print("no")
