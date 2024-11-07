



a,b,c =  list(map(int,input().split(" "))) 
d = list(map(int,input().split(" ")))

ans = b + c 

for count,i in enumerate(d):
    if i == ans:
        print(count + 1)
        break





