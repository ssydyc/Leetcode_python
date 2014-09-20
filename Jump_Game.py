class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
    # as a DP problem
        max_jump=0
        current=0
        while current<=max_jump and max_jump<=len(A)-1:
            max_jump=max(max_jump,current+A[current])
            current+=1
        if max_jump>=len(A)-1:
            return True
        else:
            return False
            
