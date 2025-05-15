l=list(map(int,input().split()))
sum=0
for i in range(len(l)):
    if i%2!=0 and l[i]%2==0:
        sum+=l[i]
print(sum)