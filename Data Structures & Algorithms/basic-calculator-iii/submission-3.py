class Solution:
    def calculate(self, s: str) -> int:
        result = 0 
        s = s.replace(" ","")
        s+="+"#flushes the buffer to the stack 
        stack = []
        idx = 0
        prev_op = ""
        while idx<len(s):
            character = s[idx]
            if character.isnumeric():
                result=result*10+int(character)
            else:
                expression = ""
                pointer = idx+1
                bracket_count =0 
                if character=="(":
                    bracket_count=1
                    while(pointer<len(s)):
                        if s[pointer]=="(":
                            bracket_count+=1
                        if s[pointer]==")":
                            bracket_count-=1
                        if bracket_count==0:
                            break
                        expression = expression+s[pointer]
                        pointer+=1
                    result = self.calculate(expression)

                    idx = pointer+1
                    continue
                if len(stack) and prev_op=="*":
                    number = stack.pop()
                    result= number*result 
                elif len(stack) and prev_op=="/":
                    number = stack.pop()
                    result = int(number/result)
                elif len(stack) and prev_op=="-":
                    result*=-1
                stack.append(result)
                result = 0 
                prev_op = character
            idx+=1
        return sum(stack)
        