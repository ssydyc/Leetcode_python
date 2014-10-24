# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        max_size=0
        for point1 in points:
            line_slope={}
            point_base=0
            for point2 in points:
                if point1.x==point2.x and point1.y==point2.y:
                    point_base+=1
                elif point1.x==point2.x:
                    if float('Inf') in line_slope:
                        line_slope[float('Inf')]+=1
                    else:
                        line_slope[float('Inf')]=1
                else:
                    temp_slope=float(point1.y-point2.y)/(point1.x-point2.x)
                    if temp_slope in line_slope:
                        line_slope[temp_slope]+=1
                    else:
                        line_slope[temp_slope]=1
            max_size=max(max_size,point_base)
            for key in line_slope:
                max_size=max(max_size,point_base+line_slope[key])
        return max_size
            
