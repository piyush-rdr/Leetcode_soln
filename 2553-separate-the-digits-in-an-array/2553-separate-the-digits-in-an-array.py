class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        arr = []

        for i in range(len(nums)):
            temp = []

            while nums[i] != 0:
                temp.append(nums[i] % 10)
                nums[i] = nums[i] // 10

            for j in range(len(temp) - 1, -1, -1):
                arr.append(temp[j])

        return arr

