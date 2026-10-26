class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==1:
            return False
        brackets_stack = []
        for bracket in s:
            if bracket=="[":
                brackets_stack.append("]")
            elif bracket=="(":
                brackets_stack.append(")")
            elif bracket=="{":
                brackets_stack.append("}")
            else:
                if not brackets_stack or (bracket!=brackets_stack[-1]):
                    return False
                else:
                    brackets_stack.remove(bracket)
        return len(brackets_stack)==0
            
        