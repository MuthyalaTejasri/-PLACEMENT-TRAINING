def fun(n,m=1):
    if n==0:
        return
    fun(n-1)
    if n%2!=0:
        print(n,end=" ")
        
    
n=100
fun(n)

