"""
1, 2, 3, 5, and 7 = 0 holes.
0, 4, 6, and 9 = 1 hole.
8 = 2 holes.
"""
n=input("enter the value for counting holes")
zero,one,two="12357","0469","8"
zero_count=0
one_count=0
two_count=0
total=0

for i in n:
    for j in zero:
        if(i==j):
            zero_count=0
    for j in one:
        if(i==j):
            one_count=one_count+1
    for j in two:
        if(i==j):
            two_count=two_count+2
total=zero_count+one_count+two_count
print("the total number of holes is",total)
    