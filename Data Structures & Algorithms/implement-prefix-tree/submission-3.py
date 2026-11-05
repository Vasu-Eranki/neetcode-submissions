class PrefixTree:

    def __init__(self):
        self.hashmap = {}

    def insert(self, word: str) -> None:
        hashmap = self.hashmap
        for character in word:
            if character not in hashmap:
                hashmap[character] = {}
            hashmap = hashmap[character]
        hashmap["#"]=True
    def search(self, word: str) -> bool:
        hashmap = self.hashmap
        for character in word:
            if character not in hashmap:
                return False
            hashmap = hashmap[character]
        return "#" in hashmap
        

    def startsWith(self, prefix: str) -> bool:
        hashmap = self.hashmap
        for character in prefix:
            if character not in hashmap:
                return False
            hashmap = hashmap[character]
        return True
        
        