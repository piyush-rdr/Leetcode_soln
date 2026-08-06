class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(nums)
        keep={}
        for i in range(0,n):
            self= target-nums[i]
            if self in keep:
                return[keep[self],i]
            keep[nums[i]]=i
