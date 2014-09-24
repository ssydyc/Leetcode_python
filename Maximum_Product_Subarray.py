class Solution:
    # @param A, a list of integers
    # @return an integer
    def multip_A(self,A,i,j): #return the multiplication of A
        if i>j: return None #no numbers
        result=1
        for k in range(i,j+1):
            result*=A[k]
        return result
        
    def no_zero_maxProduct(self,A):
        num_negtive=0
        first_negtive=-1
        last_negtive=-1
        for i in range(len(A)):
            if A[i]<0:
                if first_negtive==-1: first_negtive=i
                last_negtive=i
                num_negtive+=1
        if num_negtive%2==0:
            return self.multip_A(A,0,len(A)-1)
        else:
            if num_negtive==1 and len(A)==1: return A[0] # the only case return a negative one
            return max(self.multip_A(A,0,last_negtive-1),self.multip_A(A,first_negtive+1,len(A)-1))
            
    def maxProduct(self, A):
        result=None
        begin=0
        for i in range(len(A)):
            if A[i]==0:
                result=max(result,0)
                result=max(result,self.no_zero_maxProduct(A[begin:i]))
                begin=i+1
        if result==None:
            result=self.no_zero_maxProduct(A[begin:])
        else:
            result=max(result,self.no_zero_maxProduct(A[begin:]))
        return result
        
        
        
        
