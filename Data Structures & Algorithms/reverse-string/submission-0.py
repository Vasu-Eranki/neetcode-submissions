class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        for i in range(0,length//2):
            s[i],s[length-1-i] = s[length-1-i],s[i]
        
        