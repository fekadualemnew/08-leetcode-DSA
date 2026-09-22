class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        from collections import Counter
        n = len(nums)
        result = []
        counter = Counter(nums)
        for key, value in counter.items():
            if value > n / 3:
                result.append(key)
        return result