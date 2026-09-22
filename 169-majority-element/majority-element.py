class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        hash_dict = {}

        for item in nums:
            if item not in hash_dict:
                hash_dict[item] = 1
            elif item in hash_dict:
                hash_dict[item] += 1
        for key, value in hash_dict.items():
            if value > len(nums) / 2:
                return key

