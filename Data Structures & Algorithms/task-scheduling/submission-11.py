class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = {}
        for t in tasks:
            counter[t] = counter.get(t,0)+1
        item_freq_mapping = [(v,k) for k,v in counter.items()]
        heapq.heapify_max(item_freq_mapping)
        queue = []
        number_of_cycles = 0
        while(len(queue) or len(item_freq_mapping)): # there are still elements left to process in one of them
            if queue:
                while(queue and queue[0][0]<=number_of_cycles):
                    cycles,value,task = queue[0]
                    heapq.heappush_max(item_freq_mapping,(value,task))
                    queue.pop(0)
            if item_freq_mapping:
                value,task = heapq.heappop_max(item_freq_mapping)
                if value-1>0:
                    queue.append((number_of_cycles+n+1,value-1,task))
            number_of_cycles+=1
                


        return number_of_cycles
        