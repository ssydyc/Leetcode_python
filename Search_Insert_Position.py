'''
Created on Feb 3, 2014

@author: songsi
'''
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        if A==[]: return 0
        if A[len(A)-1]<target: return len(A)
        l=-1
        r=len(A)-1
        while l+1<r:
            m=(l+r)/2
            if A[m]<target:
                l=m
            else:
                r=m
        return r