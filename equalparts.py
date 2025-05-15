#codeforces4a watermelon into equal parts
w=int(input("Enter the weight of the watermelon:"))
if w%2!=0:
    print("NO")
else:
    x=w//2
    if(x%2==0):
        print(x,x)
    else:
        print(x-1,x+1)