class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]
        for num in nums:
            counts[num] += 1

        idx = 0
        for color in range(3):
            for _ in range(counts[color]):
                nums[idx] = color
                idx += 1

            
        