class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            p=1
            m=n
            while m!=0:
                p*=m%10
                m=m//10
            if p%t!=0:
                n+=1
                m+=1
                p=1
            else:
                return n
        
            
        
        
        