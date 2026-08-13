class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        arr = [1] * l

        p = 1

        for i in range(l):
            arr[i] = p
            p = p * nums[i]

        p = 1

        for i in range(l - 1, -1, -1):
            arr[i] = arr[i] * p
            p = p * nums[i]

        return arr