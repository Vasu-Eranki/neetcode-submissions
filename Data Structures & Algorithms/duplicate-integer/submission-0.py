class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}
        for i in nums:
            if(not dictionary.get(i,0)):
                dictionary[i] = 1
            else:
                return True
        return False