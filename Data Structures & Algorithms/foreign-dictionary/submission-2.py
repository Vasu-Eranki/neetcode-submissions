class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjacencyList = {c:[] for word in words for c in word}
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            minlen = min(len(word1),len(word2))
            if len(word2)<len(word1) and word1[:minlen]==word2[:minlen]:
                return "" # prefix violation
            else:
                for j in range(0,minlen):
                    if word1[j]!=word2[j]:
                        adjacencyList[word1[j]].append(word2[j])
                        break
        
        def topologicalSort(node,adjacencyList,visited,currentpath,toposort):
            nonlocal hascycle
            if node in currentpath:
                hascycle=True
                return
            if node in visited:
                return 
            neighbours = adjacencyList.get(node,[])
            visited.add(node)
            currentpath.add(node)
            for nei in neighbours:
                topologicalSort(nei,adjacencyList,visited,currentpath,toposort)
            toposort.append(node)
            currentpath.remove(node)
        possiblewords= []
        visited = set()

        currentpath = set()
        hascycle = False
        result = []
        for key in adjacencyList:
            if key not in visited:
                topologicalSort(key,adjacencyList,visited,currentpath,result)
                if hascycle:
                    return ""
        result  = "".join(result[::-1])
        return result
            
        