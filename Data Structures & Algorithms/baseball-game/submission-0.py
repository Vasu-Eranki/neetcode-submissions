class Solution:
    def calPoints(self, operations: List[str]) -> int:
        running_stack = []
        for i in operations:
            if i=="C":
                running_stack.pop();
            elif i=="+":
                running_stack.append(running_stack[-1]+running_stack[-2])
            elif i=="D":
                running_stack.append(running_stack[-1]*2)
            else:
                running_stack.append(int(i))
        return sum(running_stack)

        