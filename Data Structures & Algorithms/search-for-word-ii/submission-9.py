class Trie:
    def __init__(self):
        self.hashmap = {}
    def insert(self,word):
        hashmap = self.hashmap 
        for character in word:
            if character not in hashmap:
                hashmap[character] = {}
            hashmap = hashmap[character]
        hashmap["#"]=True
    def getHashmap(self):
        return self.hashmap
class Solution:
    def dfs(self,board: List[List[str]],i:int,j:int,prefix:str,hashmap:dict[str,str],results:list[str],visited:set[tuple[int,int]])->None:
        if "#" in hashmap: # we have matched all the way to the end of a word
            results.append(prefix)
            del hashmap['#']
        directions = [(0,1),(0,-1),(1,0),(-1,0)] # right, left, down, up
        ROWS = len(board)
        COLS = len(board[0])
        visited.add((i,j))
        for x,y in directions:
            delta_x = i+x 
            delta_y = j+y 
            if delta_x>=0 and delta_x<ROWS and delta_y>=0 and delta_y<COLS:
                if ((delta_x,delta_y) not in visited):
                    character = board[delta_x][delta_y]
                    if character in hashmap:
                        self.dfs(board,delta_x,delta_y,prefix+character,hashmap[character],results,visited)
        visited.remove((i,j))
        return

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        results = []
        visited = set()
        ROWS = len(board)
        COLS = len(board[0])
        hashmap = trie.getHashmap()
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] in hashmap:
                    if ((i,j) not in visited):
                        prefix = board[i][j]
                        self.dfs(board,i,j,prefix,hashmap[prefix],results,visited)
        return results
