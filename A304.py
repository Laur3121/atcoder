a=int(input())
b = []
c=[]

for n in range(a):
    left,right = list(input().split(" "))
    b.append(left)
    c.append(int (right))

n =0
min_value = min(c)
for i in range(a):
    if min_value != c[n]:   
       n+=1
    break

value = n+1 

for i in range(a):
    if value!=a:
        print(b[value])
        value+=1

value = 0

for i in range(a):
    if value < n+1:
        print(b[value])
        value+=1