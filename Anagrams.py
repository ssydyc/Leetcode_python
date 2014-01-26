'''
Created on Jan 25, 2014

@author: songsi
'''
class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        groups={}
        for temp in strs:
            key=("").join(sorted(temp))
            if key in groups:
                groups[key].append(temp)
            else:
                groups[key]=[temp]
        result=[]
        for temp in groups:
            if len(groups[temp])>1:
                for temp_str in groups[temp]:
                    result.append(temp_str)
        return result