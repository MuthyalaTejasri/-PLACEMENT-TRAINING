# "Calculating XOR of Numbers from 1 to N using Pattern"
n=int(input())
if n%4==1:
    print(1)
if n%4==2:
    print(n+1)
if n%4==3:
    print(0)
if n%4==0:
    print(n)

l=int(input())
r=int(input())
a=XoR(r)
b=XoR(l-1)
print(a^b)
