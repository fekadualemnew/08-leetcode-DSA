class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        max_height = max(heights)
        array_height = [0] * (max_height + 1)
        array_name = [0] * (max_height + 1)
        result = []

        for item in heights:
            array_height[item] += 1
            array_name[item] = names[heights.index(item)]

        for i in range(len(array_height) - 1, -1, -1):
            if array_height[i] != 0:
                result.append(array_name[i])

        return result
        