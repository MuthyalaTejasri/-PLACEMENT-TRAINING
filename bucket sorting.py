# This code counts the frequency of each element in the list a and stores the elements in separate lists based on their frequencies.

a=[5,3,3,5,2,2,2,2,1,1,4,4,3,1]
dict={}
for i in a:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1
m=max(dict.values())
b=[[] for i in range(m+1)]
for i in dict:
   b[dict[i]].append(i)
   
res=[]
print(b)
for i in range(1,len(b)):
    for j in b[i]:
        res.extend([j]*i)
print(res)