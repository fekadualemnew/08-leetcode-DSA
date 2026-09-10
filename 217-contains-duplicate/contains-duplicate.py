class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for item in nums:
            if item not in hashset:
                hashset.add(item)
            else:
                 return True
                 break
        return False
        
