a = int(input())
s = input()

""" print(s.count('T'))

n = s.count("T")
print(n)
 """

countT = 0
for i in s:
    if i == "T":
        countT += 1

countA = 0
for i in s:
    if i == "A":
        countA += 1
    



if countT == countA:
    if s[a-1] == ("T"):
        print("A")
    else: print("T")
elif countT > countA:
    print ("T")
else: 
    print("A")






