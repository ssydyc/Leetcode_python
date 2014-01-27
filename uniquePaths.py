class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        temp1=temp2=result=1
        for i in range(1,m):
            temp1=n-1+i
            temp2=i
            result=long(result*temp1)/temp2
        return int(result)
    
test=Solution()
print test.uniquePaths(2, 1)
print 2**31