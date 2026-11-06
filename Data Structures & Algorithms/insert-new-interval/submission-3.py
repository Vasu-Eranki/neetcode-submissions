class Solution:
    def binarySearch(self,intervals:List[List[int]],newInterval:List[int])->int:
        left = 0 
        right = len(intervals)-1
        target = newInterval[0]
        while (left<=right):
            mid = left + (right-left)//2
            if intervals[mid][0]==target:
                return mid
            elif intervals[mid][0]<target:
                left = mid+1
            else:
                right = mid -1
        return left
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        insert_idx = self.binarySearch(intervals,newInterval)
        intervals.insert(insert_idx,newInterval)
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
            
        