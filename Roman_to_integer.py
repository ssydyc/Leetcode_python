'''
Created on Jan 21, 2014

@author: songsi
'''
class Solution:
    # @return an integer
    def romanToInt(self, s):
        if s=='': return 0
        result=0
        for i in range(0,len(s)-1):
            if self.convert_num(s[i])>=self.convert_num(s[i+1]):
                result+=self.convert_num(s[i])
            else: result-=self.convert_num(s[i])
        result+=self.convert_num(s[len(s)-1])
        return result
        
        
    def convert_num(self,s):
        if s=='I': return 1
        elif s=='V': return 5
        elif s=='X': return 10
        elif s=='L': return 50
        elif s=='C': return 100
        elif s=='D': return 500
        elif s=='M': return 1000
        
test=Solution()
print test.romanToInt("XXX")