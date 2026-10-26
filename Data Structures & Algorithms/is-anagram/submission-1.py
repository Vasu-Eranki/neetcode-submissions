class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        character_book = {}
        for c in s:
            character_book[c] = character_book.get(c,0)+1
        for c in t:
            character_book[c] = character_book.get(c,0) -1 
            if character_book[c]<0:
                return False    
        for v in character_book.values():
            if v>0:
                return False
        return True