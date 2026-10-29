"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        hashmap = {}
        for x in intervals:
            hashmap[x.start] = hashmap.get(x.start,0)+1
            hashmap[x.end] = hashmap.get(x.end,0)-1
        meeting_rooms = 0
        max_meeting_rooms = 0
        for key in sorted(hashmap.keys()):
            meeting_rooms +=hashmap[key]
            max_meeting_rooms = max(max_meeting_rooms,meeting_rooms)
        return max_meeting_rooms==1
