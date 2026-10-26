class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while(len(stones)>1):
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if(x!=y):
                heapq.heappush(stones,-1*abs(x-y))
            else:
                heapq.heappush(stones,0)
        return -1*heapq.heappop(stones)
        