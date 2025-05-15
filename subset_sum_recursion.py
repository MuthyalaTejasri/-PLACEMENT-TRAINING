def fun(arr,i,k):
    if  k==0:
        return True
    if i==0:
        return False
    if arr[i-1]>k:
        return fun(arr,i-1,k)
    return fun(arr,i-1,k) or fun(arr,i-1,k-arr[i-1])
l=[1,2,3,8]
k=7
print(fun(l,len(l),k))