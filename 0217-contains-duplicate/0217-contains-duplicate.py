class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        k=len(nums)
        nums.sort()
        for i in range (0,k-1):
            if nums[i+1]==nums[i]:
                return True
        return False
                
        
        
       
            

            
           
            




        