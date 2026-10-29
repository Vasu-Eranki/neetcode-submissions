class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
        intervals = list(sorted(intervals,key=lambda x:x[0]))
        start1,end1 = intervals[0]
        results = []
        for i in range(1,len(intervals)):
            start2,end2 = intervals[i]
            if(start2<=end1):
                end1 = max(end1,end2) 
            else:
                results.append([start1,end1])
                start1 = start2
                end1 = end2
        results.append([start1,end1])     
        return results