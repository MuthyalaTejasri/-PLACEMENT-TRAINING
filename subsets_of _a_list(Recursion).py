def fun(arr,i=0,res=[]):
    if i==len(arr):
        print(res)
        return
    fun(arr,i+1,res+[arr[i]])
    fun(arr,i+1,res)
l=[1,2,3]
fun(l)