class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        sign=0
        result=[0]*32
        for temp in A:
            if temp<0: 
                sign+=1
                if sign==3: sign=0
                temp=-temp
            for i in range(32):
                result[i]+=(temp & 1)
                temp=temp>>1
                if result[i]==3:
                    result[i]=0
                if temp==0: break
        final_result=0
        for i in range(31,-1,-1):
            final_result=(final_result<<1) | result[i]
        if sign==0: return final_result
        else: return -final_result
