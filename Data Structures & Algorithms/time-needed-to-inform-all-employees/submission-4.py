class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        queue = [(0,headID)]
        adjancencyList ={i:[] for i in range(n)}
        for idx,i in enumerate(manager):
            if i!=-1:
                adjancencyList[i].append(idx)
        max_time = 0
        while(queue):
            length = len(queue)
            for _ in range(length):
                time_already_taken,manager_id = queue.pop(0)
                if time_already_taken>max_time:
                    max_time=time_already_taken 
                delay_time = informTime[manager_id]
                reports_underneath_them = adjancencyList[manager_id]
                employees= [(time_already_taken+delay_time,i) for i in reports_underneath_them]
                queue.extend(employees)
        return max_time

