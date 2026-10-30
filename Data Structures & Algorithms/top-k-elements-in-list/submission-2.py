class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        frequency = [False]*(len(nums)+1)
        for x in nums:
            hashmap[x] = hashmap.get(x,0)+1
        for key,value in hashmap.items():
            if not frequency[value]:
                frequency[value] = [key]
            else:
                frequency[value].append(key)
        results = []
        for idx in range(len(frequency)-1,0,-1):
            if entries:=frequency[idx]:
                for e in entries:
                    results.append(e)
                    if len(results)==k:
                        return results
        return results
