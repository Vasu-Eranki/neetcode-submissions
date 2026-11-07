class Solution:
    def decodeString(self, s: str) -> str:
        if s.isalpha():
            return s
        stack = []
        for character in s:
            if character!="]":
                stack.append(character)
            else:
                prefix = ""
                while(stack[-1]!="["):
                    prefix = stack[-1]+prefix
                    stack.pop(-1)
                stack.pop()#remove the bracket 
                multiplier = 1
                number =0 
                while(stack and stack[-1].isdigit()):
                    value = int(stack.pop())
                    number+=multiplier*value
                    multiplier*=10
                stack.append(number*prefix)
        return "".join(stack)