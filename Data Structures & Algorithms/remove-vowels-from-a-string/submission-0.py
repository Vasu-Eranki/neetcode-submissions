class Solution:
    def removeVowels(self, s: str) -> str:
        s = list(s)
        for idx, character in enumerate(s):
            if s[idx] in ("a","e","i","o","u"):
                s[idx]=""
            
        return "".join(s)
