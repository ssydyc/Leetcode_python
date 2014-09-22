# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        mer_interval=[]
        cur_point=-1
        for i in range(len(intervals)):
            if intervals[i].start<newInterval.start:
                cur_point+=1
                mer_interval.append(intervals[i])
            else:
                break
        # now append newInterval after cur_point
        if cur_point==-1 or mer_interval[cur_point].end<newInterval.start: mer_interval.append(newInterval)
        else:
            mer_interval[cur_point].end=max(mer_interval[cur_point].end,newInterval.end)
        cur_point+=1 # point to the next available interval in intervals
        while cur_point<len(intervals):
            if mer_interval[-1].end<intervals[cur_point].start:
                mer_interval.append(intervals[cur_point])
            else:
                mer_interval[-1].end=max(mer_interval[-1].end,intervals[cur_point].end)
            cur_point+=1
        return mer_interval
        
        
        
        
        
        
