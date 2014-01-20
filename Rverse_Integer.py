'''
Created on Jan 19, 2014

@author: songsi
'''
class Solution:
    # @return an integer
    def reverse(self, x):
        if x<0:
            x=abs(x)
            sign=-1
        else: sign=1
        result=0
        while x>=10:
            y=x%10
            x=x/10
            result=result*10+y
        result=result*10+x
        return sign*result
    
test=Solution()
print test.reverse(123)