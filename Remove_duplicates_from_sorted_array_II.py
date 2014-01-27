'''
Created on Jan 27, 2014

@author: songsi
'''
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if A==[]: return len(A)
        i=0
        j=1
        repeat=0
        while j<len(A):
            if A[i]==A[j]:
                if repeat==0:
                    repeat+=1
                    i+=1
                    A[i]=A[j]
                else:
                    pass
            else:
                repeat=0
                i+=1
                A[i]=A[j]
            j+=1
        return i+1        