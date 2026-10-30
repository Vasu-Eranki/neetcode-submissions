class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        number_of_subarrays = 0 
        hashmap = {}
        cumsum = 0
        for i in range(0,len(nums)):
                hashmap[cumsum] = hashmap.get(cumsum,0)+1
                cumsum+=nums[i]
                number_of_subarrays+=hashmap.get(cumsum-k,0)
        return number_of_subarrays
            


        