class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {}
        results = 0
        cumsum = 0
        for x in nums:
            hashmap[cumsum] = hashmap.get(cumsum,0)+1
            cumsum+=x
            diff = cumsum -k
            results+=hashmap.get(diff,0)


        return results