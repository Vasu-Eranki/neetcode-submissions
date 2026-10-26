class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        calculator = []
        for number in tokens:
            if number=="+":
                value1 = calculator.pop()
                value2 = calculator.pop()
                calculator.append(value1+value2)
            elif number =="-":
                value1 = calculator.pop()
                value2 = calculator.pop()
                calculator.append(value2-value1)
            elif number =="*":
                value1 = calculator.pop()
                value2 = calculator.pop()
                calculator.append(value1*value2)
            elif number =="/":
                value1 = calculator.pop()
                value2 = calculator.pop()
                resultant = value2/value1
                if(resultant<=0):
                    resultant = math.ceil(resultant)
                else:
                    resultant = math.floor(resultant)
                calculator.append(resultant)
            else:
                calculator.append(int(number))
        return calculator[-1]
        