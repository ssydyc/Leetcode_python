class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        if len(num)==1:
            return num[0]
        left,right=0,len(num)-1
        if num[right]>num[left]: return min(num[left],num[right])
        while right-left>1:
            mid=(right+left)/2
            if num[mid]>num[left]:
                left=mid
            else:
                right=mid
        return min(num[left],num[right])
