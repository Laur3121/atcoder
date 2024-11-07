import math

a,b = list(map(int,input().split(" ")))
c = 0
c = a/b
c = math.floor(c)
print (c)

if  c*b == a:
    print(c)
else: print(c+1)
