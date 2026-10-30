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
        numbers_to_add = k
        for idx in range(len(frequency)-1,0,-1):
            if entries:=frequency[idx]:
                number_of_entries = len(entries)
                if(len(entries)>numbers_to_add):
                    results.extend(entries[:numbers_to_add])
                    break
                else:
                    results.extend(entries)
                    numbers_to_add -=number_of_entries
        return results
