class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        if not A: return 0
        max_product,min_product=A[0],A[0]
        result=A[0]
        for (i,v) in enumerate(A):
            if i==0: continue
            temp=max_product
            max_product=max(temp*v,v,min_product*v)
            min_product=min(temp*v,v,min_product*v)
            result=max(max_product,result)
        return result
