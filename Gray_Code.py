class Solution:
    # @return a list of integers
    def grayCode(self, n):
        if n==0: return [0]
        result=[]
        rec_res=self.grayCode(n-1)
        for temp in rec_res:
            result.append(temp)
        for i in range(len(rec_res)-1,-1,-1):
            result.append(rec_res[i]+(1<<(n-1)))
        return result
