'''
Created on Jan 23, 2014

@author: songsi
'''

class Solution:
    # @return a boolean
    def isValid(self, s):
        stack=[]
        for temp in s:
            if temp=='(' or temp=='[' or temp=='{':
                stack.append(temp)
            else:
                if stack==[]: return False
                temp2=stack.pop()
                if temp2=='(' and temp!=')': return False
                if temp2=='[' and temp!=']': return False
                if temp2=='{' and temp!='}': return False
        if stack!=[]: return False
        return True
    
    
test=Solution()
print test.isValid("([])")