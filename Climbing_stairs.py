'''
Created on Jan 25, 2014

@author: songsi
'''
class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        result=[]
        result.append(1)
        result.append(1)
        for i in range(2,n+1):
            result.append(result[i-1]+result[i-2])
        return result[n]