class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacentList = {}
        for src in range(numCourses):
            adjacentList[src] = []
        for src,dest in prerequisites:
            adjacentList[src].append(dest)
        visited = set()
        currentpath = set()
        topologicalSort = []
        hasCycle = False
        
        def dfs(src,adjacentList,visited,topologicalSort,currentpath):
            nonlocal hasCycle
            if src in currentpath:
                hasCycle = True
                return 
            if src in visited:
                return 
            currentpath.add(src)
            visited.add(src)
            neighbours = adjacentList[src]
            for dest in neighbours:
                dfs(dest,adjacentList,visited,topologicalSort,currentpath)
            topologicalSort.append(src)
            currentpath.remove(src)
            return 
        for src in range(numCourses):
            dfs(src,adjacentList,visited,topologicalSort,currentpath)
        return topologicalSort if not hasCycle else []