class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
 
    def mysubset(self,S):    
        if len(S)==0: return [[]]
        result=[]
        x=S.pop()
        for temp in self.mysubset(S):
            if temp not in result:
                result.append(temp)
            temp=list(temp) #we need a new one
            temp.append(x)
            if temp not in result:
                result.append(temp)
        return result
        
    def subsetsWithDup(self, S):
         S.sort()
         return self.mysubset(S)
