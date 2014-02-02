'''
Created on Feb 2, 2014

@author: songsi
'''
class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        result_length=0
        before=0
        front=0
        current=0
        while front<len(s):
            if s[front]=='(': current+=1
            else: current-=1
            if current<0:
                front+=1
                before=front
                current=0
            elif current==0:
                result_length=max(result_length,front-before+1)
                front+=1
            else:
                front+=1
                
        front=before=len(s)-1
        current=0
        while front>-1:
            if s[front]==')': current+=1
            else: current-=1
            if current<0:
                front-=1
                before=front
                current=0
            elif current==0:
                result_length=max(result_length,-front+before+1)
                front-=1
            else:
                front-=1
        return result_length
    
test=Solution()
print test.longestValidParentheses("(()")