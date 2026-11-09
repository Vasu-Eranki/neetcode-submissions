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

                print(result)
            else:
                if stack and stack[-1]=="*":
                    stack.pop()
                    number = stack.pop()
                    result = number*result
                elif stack and stack[-1]=="/":
                    stack.pop()
                    number = stack.pop()
                    if number<0:
                        result = math.floor(abs(number)//result)
                        result*=-1
                    else:
                        result = math.floor(abs(number)//result)
                elif stack and stack[-1]=="-":
                    stack.pop()
                    result = -result
                stack.append(result)
                multiplier = 1
                if character=="-":
                    stack.append(character)
                elif character=="*":
                    stack.append(character)
                elif character=="/":
                    stack.append(character)
                result = 0
        return sum(stack)



