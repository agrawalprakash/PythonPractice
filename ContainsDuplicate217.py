class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Sorting is O(nlogn) or using Hashset
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
        
        
        
