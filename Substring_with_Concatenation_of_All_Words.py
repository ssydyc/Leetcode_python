'''
Created on Jan 31, 2014

@author: songsi
'''
class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        result=[]
        if S=="" or L==[]: return result
        each_length=len(L[0])
        total=len(L)
        mydict=set(L)
        temp_L={}
        temp_dict={}
        for temp in L:
            if temp in temp_dict:
                temp_dict[temp]+=1
            else:
                temp_dict[temp]=1
        #initialize the temp thing
        for i in range(each_length):
            if i+each_length*total-1>=len(S): pass
            else:
                temp_L=dict.copy(temp_dict)
                for j in range(total):
                    temp=S[i+each_length*j:i+each_length*(j+1)]
                    if temp in mydict:
                        if temp in temp_L:
                            temp_L[temp]-=1
                        else:
                            temp_L[temp]=-1
                        if temp_L[temp]==0: del temp_L[temp] 
                j=i
                if len(temp_L)==0: result.append(j)
                while j+each_length*(total+1)-1<len(S):
                    temp=S[j:j+each_length]
                    if temp in mydict:
                        if temp in temp_L:
                            temp_L[temp]+=1
                        else:
                            temp_L[temp]=1
                        if temp_L[temp]==0: del temp_L[temp]
                    j=j+each_length 
                    temp=S[j+each_length*(total-1):j+each_length*total]
                    if temp in mydict:
                        if temp in temp_L:
                            temp_L[temp]-=1
                        else:
                            temp_L[temp]=-1
                        if temp_L[temp]==0: del temp_L[temp]
                    if len(temp_L)==0: result.append(j) 
        return sorted(result)
    
            
test=Solution()
print test.findSubstring("abababab", ["ab","ab","ab"])