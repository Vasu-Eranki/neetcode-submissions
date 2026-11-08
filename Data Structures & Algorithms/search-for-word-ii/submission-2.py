class Trie:
    def __init__(self):
        self.hashmap = {}
    def put(self,word:str)->None:
        hashmap = self.hashmap 
        for idx,character in enumerate(word):
            if character not in hashmap:
                hashmap[character] = {}
            hashmap = hashmap[character]
        hashmap['#']=True
    def search(self,word:str)->bool:
        hashmap = self.hashmap 
        for idx,character in enumerate(word):
            if character not in self.hashmap:
                return False
            hashmap = hashmap[character]
        return hashmap.get(-1,False)
    def prune(self,word):
        
        def recursive(word,hashmap)->None:
            if word=="":
                del hashmap["#"]
            else:
                character = word[0]
                substring = word[1:]
                recursive(substring,hashmap[character])
                del hashmap[character]
            return
        recursive(word,self.hashmap)
        return
    def startswith(self,character:str)->bool:
        return character in self.hashmap
    def getTrieForOneWord(self,character:str)->"Trie":
        return self.hashmap[character]
class Solution:
    def dfs(self,board: List[List[str]],prefix:str,i,j,trie:dict[str,str],visited:set,results:set)->bool:
        if "#" in trie:
            results.add(prefix)
        ROWS = len(board)
        COLS = len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        queue = [(i,j,board[i][j],trie)]
        visited.add((i,j))
        for x,y in directions:
            delta_x = x+i 
            delta_y = y+j 
            if delta_x>=0 and delta_x<ROWS and delta_y>=0 and delta_y<COLS:
                character = board[delta_x][delta_y]
                if character in trie:
                    if (delta_x,delta_y) not in visited:
                        self.dfs(board,prefix+character,delta_x,delta_y,trie[character],visited,results)
        visited.remove((i,j))

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.put(word)
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        results = set()
        for i in range(ROWS):
            for j in range(COLS):
                if trie.startswith(board[i][j]):
                    trienode_for_that_word = trie.getTrieForOneWord(board[i][j])
                    self.dfs(board,board[i][j],i,j,trienode_for_that_word,visited,results)
        return list(results)

                

        