class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        i = 0
        j = n - 1
        res = []
        while i <= j:
            if height[i] <= height[j]:
                area = height[i] * (j - i)
                res.append(area)
                i += 1
            else:
                area = height[j] * (j - i)
                res.append(area)
                j -= 1
        max_value = 0
        for item in res:
            if item > max_value:
                max_value = item
        return max_value