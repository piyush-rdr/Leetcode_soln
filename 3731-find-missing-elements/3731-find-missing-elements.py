class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:

        s=min(nums)
        l=max(nums)
        full=[]
        
        for i in range(s,l+1):
            full.append(i)
            
        j=len(full)
        miss=[]
        
        for i in range(0,j):
            if full[i] not in nums:
                miss.append(full[i])
                
        return miss
        if full == nums:
            return []        

                            


