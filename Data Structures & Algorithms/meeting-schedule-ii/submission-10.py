"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starttimes = [i.start for i in intervals]
        endtimes = [i.end for i in intervals]
        starttimes.sort()
        endtimes.sort()
        current_rooms_needed = 0 
        max_rooms_used = 0 
        idx = 0 
        jdx = 0 
        while(idx<len(starttimes)):
            if starttimes[idx]<endtimes[jdx]:
                current_rooms_needed+=1
                idx+=1
            else:
                current_rooms_needed-=1
                jdx+=1
            max_rooms_used = max(max_rooms_used,current_rooms_needed)
        return max_rooms_used
        