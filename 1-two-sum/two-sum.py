class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
       
        result = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num

            if complement in result:
                return [result[complement], i]
            
            result[num] = i
                



        