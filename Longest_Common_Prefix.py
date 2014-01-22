'''
Created on Jan 21, 2014

@author: songsi
'''
class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs)==0: return ''
        mymin=len(strs[0])
        index=0
        for i in range(1,len(strs)):
            if len(strs[i])<mymin:
                mymin=len(strs[i])
                index=i
        if mymin==0: return ''
        # match string strs[index]
        while mymin>0:
            i=0
            match=strs[index][i:i+mymin]
            found=True
            for temp in strs:
                if match==temp[0:mymin]: pass
                else: 
                    found=False
                    break
            if found:
                return match
            mymin-=1             
        return ''
    
test=Solution()
print test.longestCommonPrefix(["a","ca"])             
            