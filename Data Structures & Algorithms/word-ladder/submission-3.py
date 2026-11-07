class Solution:
    def oneletterchange(self,string1:str,string2:str)->bool:
        if len(string1)!=len(string2):
            return False
        count = 0
        for s,c in zip(string1,string2):
            if s!=c:
                count+=1
                if(count>=2):
                    return False
        return True
    def prepareList(self,wordList:List[str])->int:
        adjacencyList = {}
        for idx in range(0,len(wordList)):
            for jdx in range(idx+1,len(wordList)):
                if self.oneletterchange(wordList[idx],wordList[jdx]):
                    word1 = wordList[idx]
                    word2 = wordList[jdx]
                    if word1 not in adjacencyList:
                        adjacencyList[word1] = [word2]
                    else:
                        adjacencyList[word1].append(word2)
                    
                    if word2 not in adjacencyList:
                        adjacencyList[word2] = [word1]
                    else:
                        adjacencyList[word2].append(word1)
        return adjacencyList

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        if beginWord not in wordList:
            wordList.append(beginWord)
        adjacencyList = self.prepareList(wordList)
        parentmap = {beginWord:None}
        queue = deque([beginWord])
        visited = set()
        done = False
        results = 1
        while(queue and not done):
            results+=1
            length = len(queue)
            for _ in range(length):
                word_of_choice = queue.popleft()
                visited.add(word_of_choice)
                if word_of_choice==endWord:
                    done = True
                    return results-1
                    break
                else:
                    neighbours = adjacencyList.get(word_of_choice,[])
                    for nei in neighbours:
                        if nei not in visited:
                            queue.append(nei)
                            visited.add(nei)
        return 0