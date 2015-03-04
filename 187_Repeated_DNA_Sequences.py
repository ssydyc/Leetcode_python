class Solution:
    # @param s, a string
    # @return a list of strings
    def __init__(self):
        self.DNAhash={} # keep the linear time
    
    def duplicate(self):
        result=[]
        for temp in self.DNAhash:
            if self.DNAhash[temp]>1:
                result.append(temp)
        return result
    
    def findRepeatedDnaSequences(self, s):
        result=[]
        for i in range(len(s)):
            if i<9: continue
            temp=s[i-9:i+1]
            if temp in self.DNAhash:
                self.DNAhash[temp]+=1
            else:
                self.DNAhash[temp]=1
        return self.duplicate()
