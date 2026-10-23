class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        arr1_count = defaultdict(int)
        end = []

        for n in arr1:
            if n not in arr2:
                end.append(n)
            arr1_count[n] += 1
        end.sort()

        res = []
        
        for n in arr2:
            for _ in range(arr1_count[n]):
                res.append(n)
        
        return res + end