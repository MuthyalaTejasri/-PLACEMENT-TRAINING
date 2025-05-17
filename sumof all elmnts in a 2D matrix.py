m=[[1,2,3],
   [4,5,6],
   [7,8,9]
   ]
rows=len(m)
cols=len(m[0])
sum=0
for i in range(rows):
    for j in range(cols):
        sum+=m[i][j]
print(sum)