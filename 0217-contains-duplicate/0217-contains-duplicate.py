class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
       
        nums.sort()
        for i in range(0,len(nums)-1):
            if nums[i+1]==nums[i]:
                return True
        return False
                
        
        
       
            

            
           
            




        