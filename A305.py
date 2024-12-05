a = int(input())

n = a%5

if n in (0,1,2):
    print(a-n)
else: print(a+(5-n))
