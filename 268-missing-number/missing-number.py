class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()    
        for i in range(len(nums) + 1):
            if i < len(nums) and i != nums[i]:
                return i
            elif i == len(nums):
                return i

