class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = {}
        for t in tasks:
            hashmap[t] = hashmap.get(t,0)+1
        cycles = 0 
        max_frequency = max(hashmap.values())
        number_of_keys = sum([1 for k,v in hashmap.items() if v==max_frequency])

        return max(len(tasks),(max_frequency-1)*(n+1)+number_of_keys)
        # we have the counts for each task
        

        