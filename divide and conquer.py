def div(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=div(arr[:mid])
    right=div(arr[mid:])
    return merge(left,right)
def merge(left,right):
    res=[]
    i=0
    j=0
    while(i<len(left) and j<len(right)):
        if left[i]<right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    res.extend(left[i:])
    res.extend(right[j:])
    return res
l=[3,2,1,5,4,3]
sorted_l=div(l)
print(sorted_l)