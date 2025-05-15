n,m,a,b=map(int,input().split())
if (m*a<b):
    print(a*n)
else:
    print(((n//m)*b)+min((n%m)*a,b))