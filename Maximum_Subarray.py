class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        max_A=max(A)
        if max_A<0:
            return max_A
        max_A=0
        current_max=0
        for i in range(len(A)):
            if A[i]>=0:
                current_max+=A[i]
            else: #A[i]<0
                max_A=max(max_A,current_max)
                current_max=max(0,current_max+A[i]) #have a postive one at least
        return max(max_A,current_max)
