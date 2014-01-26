'''
Created on Jan 26, 2014

@author: songsi
'''
class Solution:
    # @return a string
    def countAndSay(self, n):
        result='1'
        for i in range(0,n-1):
            result=self.my_count(result)
        return result
            
    def my_count(self, result):
        num=0
        digit=""
        myresult=""
        for temp in result:
            if num==0:
                digit=temp
                num+=1
            elif digit==temp:
                num+=1
            else:
                myresult+=str(num)+digit
                digit=temp
                num=1
        myresult+=str(num)+digit
        return myresult      