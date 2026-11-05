class WordDictionary:

    def __init__(self):
        self.hashmap = {}        

    def addWord(self, word: str) -> None:
        hashmap = self.hashmap
        for character in word:
            if character not in hashmap:
                hashmap[character]= {}
            hashmap=hashmap[character]
        hashmap["#"]={"%":False}
    def search(self, word: str) -> bool:
        
        hashmap = self.hashmap
        def recursiveLookup(word,index,hashmap)->bool:
            if index==len(word):
                print(hashmap)
                return "#" in hashmap
            else:
                if word[index]!=".":
                    result = False 
                    if word[index] not in hashmap:
                        return False 
                    else:
                        character = word[index]
                        result = result or recursiveLookup(word,index+1,hashmap[character])
                else: # do wildcard matching 
                    result = False 
                    for character in hashmap:
                        result = result or recursiveLookup(word,index+1,hashmap[character])
            return result
        return recursiveLookup(word,0,hashmap)
