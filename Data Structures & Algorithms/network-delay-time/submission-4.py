class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjacencyList = {}
        for i in range(1,n+1):
            adjacencyList[i]= []
        for source,destination,time in times:
            adjacencyList[source].append((destination,time))
        distances = [float('inf')]*(n+1)
        distances[k]=0
        queue = [(0,k)]
        while(queue):
            #djikstra 
            curr_distance,node = heapq.heappop(queue)
            if curr_distance>distances[node]: # we have already found a cheaper route, ignoring
                continue
            neighbours = adjacencyList[node]
            for nei,distance in neighbours:
                if curr_distance+distance<distances[nei]: # if shorter, we explore further
                    distances[nei] = curr_distance+distance
                    heapq.heappush(queue,((curr_distance+distance,nei)))
        distances = distances[1:]
        return max(distances) if float('inf') not in distances else -1# remove the first element, send the maximum