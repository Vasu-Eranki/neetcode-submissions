class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for character in num:
            if stack:
                while(stack and character<stack[-1] and k>0):
                    stack.pop(-1)
                    k-=1
            stack.append(character)
        while(stack and k>0):
            stack.pop(-1)
            k-=1
        result = "".join(stack).lstrip("0")
        return  result if result else "0"