class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjacencyList = {}
        for i in range(n):
            adjacencyList[i] = {}
        for source,destination,price in flights:
            adjacencyList[source][destination] = price 
        distance_price = [[float('inf')]*(k+2) for _ in range(n)]
        queue = [(0,0,src)]
        while(queue):
            curr_price,curr_dist,node = heapq.heappop(queue)
            if(node==dst):
                return curr_price
            elif(curr_dist==k+1 or curr_price>distance_price[node][curr_dist]):
                continue
            neighbours = adjacencyList[node]
            for next_neighbour,cost in neighbours.items():
                if cost+curr_price<distance_price[next_neighbour][curr_dist+1]:
                    distance_price[next_neighbour][curr_dist+1] = cost+curr_price
                    heapq.heappush(queue,(cost+curr_price,curr_dist+1,next_neighbour))


        return -1
        