class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        results = []
        start_interval = intervals[0][0]
        end_interval = intervals[0][1]
        for idx in range(1,len(intervals)):
            if intervals[idx][0]<=end_interval: # if overlap 
                end_interval = max(intervals[idx][1],end_interval)
                start_interval = min(intervals[idx][0],start_interval)
            else:
                results.append([start_interval,end_interval])
                start_interval = intervals[idx][0]
                end_interval = intervals[idx][1]
        results.append([start_interval,end_interval])
        return results
            
        