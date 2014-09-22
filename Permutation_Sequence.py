class Solution:
    # @return a string
    def getPermutation(self, n, k):
        facto=[] #record factorial
        current=[str(i+1) for i in range(n)] # record the number exist
        result=[]
        for i in range(n):
            if i==0: facto.append(1)
            else: facto.append(facto[i-1]*i)
        k=k-1
        for i in range(n):
            to_add=k/facto[n-1-i]
            result.append(current.pop(to_add))
            k=k%facto[n-1-i]
        return ''.join(result)
