class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        number_of_subarrays = 0 
        hashmap = {0:1}
        cumsum = 0
        for i in range(0,len(nums)):
                cumsum+=nums[i]
                number_of_subarrays+=hashmap.get(cumsum-k,0)
                hashmap[cumsum] = hashmap.get(cumsum,0)+1
        return number_of_subarrays
            


        