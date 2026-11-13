class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last_index = {}
        for index, value in enumerate(s):
            last_index[value] = index

        size, end = 0, 0
        result = []

        for index, value in enumerate(s):
            size += 1
            end = max(end, last_index[value])

            if index == end:
                result.append(size)
                size = 0
        return result

