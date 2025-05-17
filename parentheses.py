#This code generates all possible valid combinations of parentheses of length 2n. Here's a breakdown:

def binary(n,res="",o=0,c=0):
    if o==n and c==n:
        print(res)
        return
    if o<n:
        binary(n,res+"(",o+1,c)
    if c<o:
        binary(n,res+")",o,c+1)
n=2
binary(n)