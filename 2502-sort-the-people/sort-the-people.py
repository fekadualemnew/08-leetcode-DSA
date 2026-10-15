class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        n = len(names)
        for i in range(n):
            for j in range(i, n):
                if heights[i] < heights[j]:
                    heights[i], heights[j] = heights[j], heights[i]
                    names[i], names[j] = names[j], names[i]

        return names
        