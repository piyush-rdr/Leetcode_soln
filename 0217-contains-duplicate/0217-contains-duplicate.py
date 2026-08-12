class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        i=0
        k=len(nums)-1
        nums.sort()
        while i<k:
            if nums[i+1]==nums[i]:
                return True
            else:
                i+=1
        return False
                
        
        
       
            

            
           
            




        