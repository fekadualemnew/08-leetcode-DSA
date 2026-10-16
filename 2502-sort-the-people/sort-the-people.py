class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        max_height = max(heights)
        
        bucket = [[] for _ in range(max_height + 1)]

        for height, name in zip(heights, names):
            bucket[height].append(name)
        
        result = []
        for h in range(max_height, -1, -1):
            if bucket[h]:
                result.extend(bucket[h])

        return result
        