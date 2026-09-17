"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        seq = sorted(intervals, key=lambda x: x.start)

        current = None
        for meeting in seq:
            if current is None:
                current = meeting
                continue
            
            if meeting.start < current.end:
                return False
            
            if meeting.end == current.start:
                current.start = meeting.end
            
            if meeting.end > current.start:
                current = meeting
        return True
