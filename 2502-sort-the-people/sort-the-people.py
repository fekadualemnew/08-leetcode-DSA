class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        name_to_height = {}
        for h, n in zip(heights, names):
            name_to_height[h] = n
        res = []

        for h in reversed(sorted(heights)):
            res.append(name_to_height[h])
       
        return res
        