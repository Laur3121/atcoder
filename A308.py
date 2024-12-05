a = list(map(int,input().split()))
i = 0
""" if  a[0]<a[1]<a[2]<a[3]<a[4] .... : """
b =0
if a == sorted(a):
    for i in range(8):
        if 100<= a[i] and a[i] <= 675:
            if a[i]%25 == 0:
                b+=1

if b == 8:
    print("Yes")
else: print("No")