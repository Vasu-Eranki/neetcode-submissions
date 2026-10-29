class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        
        adjacencylist = {}
        for i in range(0,numCourses):
            adjacencylist[i] = []
        for edge in prerequisites:
            source,dest = edge 
            adjacencylist[source].append(dest)
        visited = set()
        currentpath = set()
        hasloop=False

        def dfs(source,adjacencylist,visited,currentpath):
            nonlocal hasloop
            if source in currentpath:
                hasloop=True
                return
            if source in visited:
                return
            visited.add(source)
            currentpath.add(source)
            edges = adjacencylist[source]
            for e in edges:
                dfs(e,adjacencylist,visited,currentpath)
            currentpath.remove(source)
            return
        for i in range(0,numCourses):
            dfs(i,adjacencylist,visited,currentpath)     
        return True if hasloop==False else False
        