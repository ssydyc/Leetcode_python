'''
Created on Jan 23, 2014

@author: songsi
'''
class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        convert=[]
        for i in range(2,8):
            temp=[]
            temp.append(chr(ord('a')+(i-2)*3))
            temp.append(chr(ord('a')+(i-2)*3+1))
            temp.append(chr(ord('a')+(i-2)*3+2))
            convert.append(temp)
        convert[5].append('s')
        convert.append(['t','u','v'])
        convert.append(['w','x','y','z'])
        result=[""]
        for temp_char in digits:
            if temp_char>'9' or temp_char<'2': pass
            else:
                temp_list=[]
                for temp_add in convert[ord(temp_char)-ord('2')]:
                    for result_list in result:
                        result_list+=temp_add
                        temp_list.append(result_list)
                result=temp_list
        return result
    
test=Solution()
print test.letterCombinations("123")