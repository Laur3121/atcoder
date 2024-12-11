n = int(input())
P = list(map(int,input().split()))

diff = (max(P) - P[0])


if max(P) == P[0] and max(P) in P[1:]:
    print(1)

if max(P) == P[0] and max(P) not in P[1:]:
    print(0)

if diff > 0:
    print(diff + 1)





