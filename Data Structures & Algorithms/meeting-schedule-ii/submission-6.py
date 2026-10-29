"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starttimes = []
        endtimes = []
        for x in intervals:
            start = x.start
            end = x.end
            starttimes.append(start)
            endtimes.append(end)
        starttimes.sort()
        endtimes.sort()
        max_number_of_rooms = 0
        number_of_independent_rooms_needed = 0
        s = 0 
        e = 0 
        while(s<len(starttimes) and e<len(endtimes)):
            if starttimes[s]<endtimes[e]:
                number_of_independent_rooms_needed+=1
                s+=1
            else:
                number_of_independent_rooms_needed-=1
                e+=1
            max_number_of_rooms = max(number_of_independent_rooms_needed,max_number_of_rooms)

        return max_number_of_rooms
        