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
                print(f"character {character} stack : {stack}")
                if not stack:
                    return False
                top_of_stack = stack.pop()
                if(character=="]" and top_of_stack!='['):
                    return False
                if(character==")" and top_of_stack!="("):
                    return False
                if(character=="}" and top_of_stack!="{"):
                    return False
        return len(stack)==0

        