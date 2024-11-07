a = int(input())
s = input()

print(s)

print(s.count('T'))

for count,i in enumerate(s):
    if i == "T":
        count + 1

print(count) 


