class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        n = len(heights)
        for i in range(n):
            key = heights[i]
            temp = names[i]
            j = i - 1

            while j >= 0 and key > heights[j]:
                heights[j + 1] = heights[j]
                names[j + 1] = names[j]  
                j -= 1
            heights[j + 1] = key
            names[j + 1] = temp
        return names
        