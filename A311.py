# aが文字数、bが文字列
a = int(input())
n = list(input())

a_counter = 0
b_counter = 0
c_counter = 0

i = 0
for i in range(a):
        if (n[i] == "A"):
            a_counter+=1
        if (n[i] == "B"):
            b_counter+=1
        if (n[i] == "C"):
            c_counter+=1
        if (a_counter > 0) and (b_counter > 0) and (c_counter > 0):
            print(i+1)
            break




