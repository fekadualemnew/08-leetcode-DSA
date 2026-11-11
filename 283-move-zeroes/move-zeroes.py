class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        ptr = 0
        for i in range(n):
            if nums[ptr] != 0:
                ptr += 1
            elif nums[ptr] == 0 and nums[i] != 0:
                nums[ptr], nums[i] = nums[i], nums[ptr]
                ptr += 1
            

        