class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def sub_rotate(self,nums,n,k):
        # return the number of right shifts
        for i in range(n-1,k-1,-1):
            nums[i],nums[i-k]=nums[i-k],nums[i]
    
    def rotate(self, nums, k):
        n=len(nums)
        k=k%n
        if k==0: return
        while n%k!=0:
            self.sub_rotate(nums,n,k)
            n,k=k,k-n%k
        self.sub_rotate(nums,n,k)
