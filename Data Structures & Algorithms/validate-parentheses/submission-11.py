class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2:
            return False
        stack = []
        for character in s:
            if character=="[":
                stack.append("[")
            elif character=="(":
                stack.append("(")
            elif character=="{":
                stack.append("{")
            else:
                if not stack:
                    return False
                top_of_stack = stack.pop()
                if((character=="]" and top_of_stack!='[') or (character==")" and top_of_stack!="(") or (character=="}" and top_of_stack!="{")):
                    return False
        return len(stack)==0

        