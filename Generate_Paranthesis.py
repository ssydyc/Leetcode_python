'''
Created on Jan 24, 2014

@author: songsi
'''
class Solution:
    answer=[[""]]
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        for i in range(1,n+1):
            self.answer.append([])
            for temp in self.answer[i-1]:
                self.answer[i].append("("+temp+")")
            for j in range(1,i):
                for temp1 in self.answer[j]:
                    for temp2 in self.answer[i-j]:
                        self.answer[i].append(temp1+temp2)
            self.answer[i]=list(set(self.answer[i]))      
        return list(set(self.answer[n]))            
                        
test=Solution()
print test.generateParenthesis(3)