class Solution:
    def isGood(self, nums: List[int]) -> bool:
        l=len(nums)
        arr=[]
        for i in range(1,l):
            arr.append(i)
        arr.append(l-1)
        nums.sort()
        if arr == nums:
            return True
        else:
            return False

        