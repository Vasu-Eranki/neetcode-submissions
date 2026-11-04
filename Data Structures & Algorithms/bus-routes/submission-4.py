class Solution:
    def addentries(self,adjacencyList:dict[int,int],route:list[int]):
        for i in range(len(route)):
            source = route[i]
            for j in range(i+1,len(route)):
                dest = route[j]
                if source not in adjacencyList:
                    adjacencyList[source] = [dest]
                else:
                    adjacencyList[source].append(dest)
                if dest not in adjacencyList:
                    adjacencyList[dest] = [source]
                else:
                    adjacencyList[dest].append(source)
            

    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        adjacencyList = {}
        for busstops in routes:
            self.addentries(adjacencyList,busstops)
        number_of_stops = 0
        queue = deque([source])
        parent_map = {source:None}
        visited = set()
        if source==target:
            return 0
        if source not in adjacencyList:
            return -1
        if target not in adjacencyList:
            return -1
        while(queue):
            length = len(queue)
            for _ in range(length):
                stop = queue.popleft()
                if stop==target:
                    return number_of_stops
                neighbours = adjacencyList[stop]
                for neigh in neighbours:
                    if neigh not in visited:
                        queue.append(neigh)
                visited.add(stop)
            number_of_stops+=1
        return -1

        