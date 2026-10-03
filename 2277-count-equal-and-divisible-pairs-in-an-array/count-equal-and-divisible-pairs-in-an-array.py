class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        n = len(nums)
        count = 0

        for i in range(n):
            for j in range(n):
                if i != j and nums[i] == nums[j] and (i * j) % k == 0 and i < j:
                    count += 1
        return count
