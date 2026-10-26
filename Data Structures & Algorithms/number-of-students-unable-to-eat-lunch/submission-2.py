class Solution:
    def rotateArray(self,x):
        value = x.pop(0)
        x.append(value)
        return x

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counter = 0
        while(True):
            if(not students):
                break
            if(students[0]==sandwiches[0]):
                students = students[1:]
                sandwiches = sandwiches[1:]
                counter = 0
            else:
                students = self.rotateArray(students)
                counter+=1
                if(counter==len(students)):
                    break
        return len(students)