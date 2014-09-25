class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def mysubset(self,S):    
        if len(S)==0: return [[]]
        result=[]
        x=S.pop()
        for temp in self.mysubset(S):
            result.append(temp)
            temp=list(temp) #we need a new one
            temp.append(x)
            result.append(temp)
        return result
        
    def subsets(self, S):
        S.sort()
        return self.mysubset(S)
   
