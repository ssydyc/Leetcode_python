'''
Created on Jan 20, 2014

@author: songsi
'''
class Solution:
    # @return a boolean
    s=p=''
    def isMatch(self, s, p):
        self.s=s
        temp=''
        for i in range(0,len(p)):
            if i<len(p)-1 and p[i+1]=='*':
                if i!=0 and p[i-1]=='*' and p[i-2]==p[i]:
                    pass
                else:
                    temp=temp+p[i]
            else:
                temp=temp+p[i]
        for i in range(0,len(temp)):
            if temp[i]=='*' and temp[i-1]=='*': pass
            else: self.p=self.p+temp[i]
        return self.myMatch(0,0)

    def myMatch(self,i,j):    
        if len(self.p)-j<2 or self.p[j+1]!='*':
            #no * after the current string
            if len(self.p)-j<1 or len(self.s)-i<1: 
                if len(self.p)-j==len(self.s)-i: return True
                else: return False
            else: # both not empty
                if self.p[j]=='.' or self.s[i]==self.p[j]: 
                    return self.myMatch(i+1,j+1)
                else:
                    return False
        else:   #we have # to handle with
            result=False
            if(self.p[j]=='.'):
                for m in range(0,len(self.s)-i+1):
                    result=self.myMatch(i+m,j+2)
                    if result: return result
            else:
                for m in range(0,len(self.s)-i+1):
                    if m==0 or self.s[i+m-1]==self.p[j]:
                        result=self.myMatch(i+m,j+2)
                        if result: return result
                    else:
                        break
            return result
        
test=Solution()
print test.isMatch("aa","a")