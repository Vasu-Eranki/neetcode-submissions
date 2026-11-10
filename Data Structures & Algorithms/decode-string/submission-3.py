class Solution:
    def decodeString(self, s: str) -> str:
        if s.isalpha():
            return s
        stack = []
        for idx, character in enumerate(s):
            if character!="]":
                stack.append(character)
            else:
                left_pointer = idx-1
                substring = ""
                while(stack[-1]!="["):
                    substring = stack.pop() +substring # pop characters from stack  
                stack.pop() 
                result = 0 
                left_pointer-=1 # there's a number present there
                multiplier = 1
                while(stack and stack[-1].isnumeric()):
                    number = int(stack.pop())
                    result = result+multiplier*number
                    multiplier*=10
                stack.append(result*substring)
        return "".join(stack)

