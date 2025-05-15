def freq(l,t,i=0):
    
    if i==len(l):
        return 0
    
    if l[i]==t:
        return 1+freq(l,t,i+1)
    else:
        return freq(l,t,i+1)
l=[1,2,5,4,5,5]
t=5
print(freq(l,t))