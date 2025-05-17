class Solution:
    def trailingzeroes(self,n:int)->int:
        if(n<5):
            return 0;
        sum=0
        while(n>=5):
            sum=sum+n//5
            n=n//5
        return sum