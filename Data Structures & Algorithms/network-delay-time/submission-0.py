class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjancenyList = {}
        for i in range(1,n+1):
            adjancenyList[i] = {}
        for src,dest,cost in times:
            adjancenyList[src][dest] = cost 

        queue = [(0,k)]
        distance = [float('inf')]*(n+1)
        distance[k] = 0
        while(queue):
            curr_distance, node = heapq.heappop(queue)
            if curr_distance > distance[node]:
                continue
            neighbours =  adjancenyList[node]
            for next_node,cost in neighbours.items():
                if curr_distance+cost<distance[next_node]:
                    distance[next_node] = curr_distance+cost
                    heapq.heappush(queue,(curr_distance+cost,next_node))
        distance = distance[1:]
        return max(distance) if float('inf') not in distance else -1
