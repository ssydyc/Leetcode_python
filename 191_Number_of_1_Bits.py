class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        result=0
        while n!=0:
            n=n&(n-1)
            result+=1
        return result
