# aが商品の数,bがドリンクの値段,cが割引後のドリンクの値段
a,b,c = list(map(int,input().split()))
items = list(map(int,input().split()))

""" print (a,b,c)
print(items) """

n = 0
d = []
for n in range(a):
    d.append(c + items[n])
    n+=1

n = 0
d = sorted(d)

if b <= d[0]:
    print(b)
else:
    print(d[0])

    

