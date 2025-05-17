# This code simulates a fire spreading in a matrix m and then counts the number of cells that were not burned (i.e., cells that still have a value of 1).
def fire(m,i,j):
    if not m:
        return
    if i<0 or i>=len(m) or j<0 or j>=len(m) or m[i][j]!=1:
        return
    m[i][j]=2
    fire(m,i+1,j)
    fire(m,i-1,j)
    fire(m,i,j+1)
    fire(m,i,j-1)
m=[[1,1,1,0],
   [0,1,1,0],
   [1,0,0,0],
   [1,0,0,1]
   ]
fire(m, 0, 0)
count=0
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j]==1:
            count+=1
print(count)
