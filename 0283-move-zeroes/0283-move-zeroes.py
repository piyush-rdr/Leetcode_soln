class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        arr=[]
        i=0
        while i<l:
            if nums[i]==0:
                arr.append(nums.pop(i))
                l=l-1
            else:
                i=i+1
        for j in range(len(arr)):
            nums.append(arr[j])
