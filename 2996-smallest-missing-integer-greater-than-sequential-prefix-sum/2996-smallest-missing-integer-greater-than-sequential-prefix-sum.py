class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        
        k = len(nums)
        s = nums[0]
        j = 0

        for i in range(1, k):
            if nums[i] - nums[j] == 1:
                s += nums[i]
                j += 1
            else:
                break

        while s in set(nums):
            s += 1

        return s


       