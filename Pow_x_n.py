class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def my_pow(self,x,n):    
        if n==0: return 1
        if n%2==0: return (self.my_pow(x,n/2))**2
        else: return self.my_pow(x,(n-1)/2)**2*x
        
    def pow(self, x, n):
        if n<0: return 1./self.my_pow(x,-n)
        else: return self.my_pow(x,n)
        
