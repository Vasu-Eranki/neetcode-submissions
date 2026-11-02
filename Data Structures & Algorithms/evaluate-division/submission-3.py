class Solution:

    def bfs(self,src,dest,adjancentList)->float:
        if src not in adjancentList:
            return -1
        elif dest not in adjancentList:
            return -1
        elif src==dest:
            return 1
        visited = {src:True} # starting at source
        queue = deque([src])
        parent = {src:None}
        path = []
        found = False
        while(queue and not found):
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                visited[node]=True
                if node==dest: # we have reached destination
                    parentNode = dest
                    while(parentNode is not None):
                        path.append(parentNode)
                        parentNode = parent[parentNode]
                    found = True
                    break
                for neighbour in adjancentList[node].keys():
                    if neighbour not in visited:
                        parent[neighbour] = node
                        queue.append(neighbour)
        path = path[::-1]            
        multiplier = 1
        for i in range(0,len(path)-1):
            src,dest = path[i:i+2]
            multiplier*=adjancentList[src][dest] 

        return multiplier if path else -1
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjacentList = {}
        results = []
        for src_dest,val in zip(equations,values):
            src,dest = src_dest
            if src not in adjacentList:
                adjacentList[src] = {dest:val}
            else:
                adjacentList[src][dest]=val
            
            if dest not in adjacentList:
                adjacentList[dest] = {src:1/val}
            else:
                adjacentList[dest][src]=1/val
        results = []
        for src,dest in queries:
            results.append(self.bfs(src,dest,adjacentList))
        
        return results
        

        