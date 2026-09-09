class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        product1 = nums[-1] * nums[-2] * nums[-3]
        product2 = nums[0] * nums[1] * nums[-1]

        if product1 >= product2:
            maximum = product1
        elif product1 < product2:
            maximum = product2
        return maximum


            