class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_dict = {}

        for item in nums:
            if item in hash_dict:
                return True
            hash_dict[item] = True 
        return False

        
        
