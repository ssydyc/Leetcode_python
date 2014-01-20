'''
Created on Jan 19, 2014

@author: songsi
'''
class Solution:
    # @return a string
    def convert(self, s, nRows):
        if s=='' or nRows==1: return s
        conversion=[]
        for i in range(0,nRows):
            conversion.append('')
        line=0
        direction=0 # 0 means increase, 1 means decrease
        for char in s:
            conversion[line]+=char
            if direction==0:
                if line==nRows-1:
                    direction=1
                    line-=1
                else: line+=1
            else:
                if line==0:
                    direction=0
                    line+=1
                else: line-=1
        result=''
        for temp in conversion: 
            result+=temp
        return result
            