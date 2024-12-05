a,b =  list(map(int,input().split()))

if a in (2,5,8) or b in (2,5,8):
    if (a-1 == b) or (a+1 ==b):
        print("Yes")
    else: print("No")
else: print("No")
