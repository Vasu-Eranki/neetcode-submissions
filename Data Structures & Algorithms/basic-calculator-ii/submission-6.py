import math
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        multiplier = 1
        result = 0
        s = "".join([i for i in s if i!=" "]) # remove whitespace
        s+="+"
        for character in s:
            if character.isnumeric():
                result = result*10+int(character)
            else:
                if stack and stack[-1]=="*":
                    stack.pop()
                    number = stack.pop()
                    result = number*result
                elif stack and stack[-1]=="/":
                    stack.pop()
                    number = stack.pop()
                    result = int(number/result)
                elif stack and stack[-1]=="-":
                    stack.pop()
                    result = -result
                stack.append(result)
                if character in ("-","*","/"):
                    stack.append(character)
                result = 0
                multiplier = 1
        return sum(stack)



