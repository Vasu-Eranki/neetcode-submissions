class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for character in s:
            if character=="[":
                stack.append("]")
            elif character=="(":
                stack.append(")")
            elif character=="{":
                stack.append("}")
            else:
                if stack and stack[-1]==character:
                    stack.pop()
                else:
                    return False
        return len(stack)==0

        