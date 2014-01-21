'''
Created on Jan 21, 2014

@author: songsi
'''
class Solution:
    # @return an integer
    def maxArea(self, height):
        max_area=0
        left=0
        right=len(height)-1
        while left<right:
            temp=(right-left)*min(height[left],height[right])
            max_area=max(max_area,temp)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_area