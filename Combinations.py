class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        if n<k: return []
        if k==0: return [[]] #the only case
        if n==k: return [[i for i in range(1,k+1)]]
        result=[]
        for temp in self.combine(n-1,k-1): #select n
            temp.append(n)
            result.append(temp)
        for temp in self.combine(n-1,k):
            result.append(temp)
        return result
            
