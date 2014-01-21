'''
Created on Jan 21, 2014

@author: songsi
'''
class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        if len(A)==0: return 1
        for i in range(0,len(A)):
            while A[i]!=i+1 and A[i]>0 and A[i]<=len(A) and A[i]!=A[A[i]-1]:
                #swap A[i] and A[A[i]-1]
                temp=A[i]
                A[i]=A[A[i]-1]
                A[temp-1]=temp
        for i in range(0,len(A)):
            if A[i]!=i+1 :
                return i+1
        return len(A)+1    
            
test=Solution()
print test.firstMissingPositive([-4,24,32,25,16,-8,3,-5,-6,30,3,3,29,-5,6,-3,1,29,-2,4,4,7,14,20,5,0,25,2,13,26,-9,7,6,33])