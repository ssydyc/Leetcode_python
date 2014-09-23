class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        result=[]
        a_len=len(a)
        b_len=len(b)
        if a_len>b_len:
            b,a=a,b #let b always be longer
        for i in range(len(b)-len(a)):
            result.append(int(b[i]))
        for i in range(len(a)):
            result.append(int(b[i+len(b)-len(a)])+int(a[i]))
        to_add=0
        for i in range(len(b)-1,-1,-1):
            result[i]+=to_add
            to_add=0
            if result[i]>=2:
                result[i]-=2
                to_add=1
            result[i]=str(result[i])
        if to_add==1: result.insert(0,'1')
        return ''.join(result)
    
