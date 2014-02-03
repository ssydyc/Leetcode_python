class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        #binary search
        if A=='': return -1
        l=0
        r=len(A)-1
        if A[l]==target: return l
        if A[r]==target: return r
        while l+1<r:
            m=(l+r)/2
            #print A[m]
            if A[m]==target: return m
            elif A[m]>A[len(A)-1]:
                if target>A[m]: l=m+1
                elif target>A[0]: r=m-1
                else: l=m+1
            else:
                if target<A[m]: r=m-1
                elif target>A[len(A)-1]: r=m-1
                else: l=m+1
        if A[l]==target: return l
        if A[r]==target: return r
        return -1
    
    
test=Solution()
print test.search([4,5,6,7,0,1,2], 0)