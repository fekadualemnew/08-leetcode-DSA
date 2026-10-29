class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        result = []
        for i in range(len(nums)):
            sum = 0
            for j in range(len(nums)):
                if j != i and nums[j] < nums[i]:
                    sum += 1
            result.append(sum)
        return result