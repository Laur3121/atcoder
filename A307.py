i = int(input())
data = list(map(int,input().split(" ")))

n = 0

for _ in range(i):
    print(sum(data[n:n+7]),end=" ")
    n= n+7