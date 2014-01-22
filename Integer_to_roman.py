'''
Created on Jan 21, 2014

@author: songsi
'''
class Solution:
    # @return a string
    def intToRoman(self, num):
        result=''
        result+='M'*(num/1000)
        num=num%1000
        hundred=num/100
        if hundred>0 and hundred<=3:
            for i in range(0,hundred):
                result+='C'
        if hundred==4:
            result+='CD'
        if hundred==9:
            result+='CM'
        if hundred>4 and hundred<9:
            result+='D'
            result+='C'*(hundred-5)
        num=num%100
        hundred=num/10            
        if hundred>0 and hundred<=3:
            for i in range(0,hundred):
                result+='X'
        if hundred==4:
            result+='XL'
        if hundred==9:
            result+='XC'
        if hundred>4 and hundred<9:
            result+='L'
            result+='X'*(hundred-5)
        num=num%10
        hundred=num/1
        if hundred>0 and hundred<=3:
            for i in range(0,hundred):
                result+='I'
        if hundred==4:
            result+='IV'
        if hundred==9:
            result+='IX'
        if hundred>4 and hundred<9:
            result+='V'
            result+='I'*(hundred-5)
        return result