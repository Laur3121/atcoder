import math

a,b = list(map(int,input().split(" ")))
c = 0
c = a//b   
""" 浮動小数点直し """
c = math.floor(c)

if  c*b == a:
    print(c)
else: print(c+1)

