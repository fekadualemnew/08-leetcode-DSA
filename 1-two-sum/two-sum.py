class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = []

        for i in range(len(nums)):
            if (target - nums[i]) in nums and i != nums.index(target - nums[i]):
                result.append(i)
                result.append(nums.index(target - nums[i]))
                return result
        