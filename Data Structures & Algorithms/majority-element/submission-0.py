class Solution:

    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for number in nums:
            hashmap[number] = hashmap.get(number,0)+1
        result = None
        for key,value in hashmap.items():
            if value>len(nums)//2:
                result= key
                break
        return result

        
        