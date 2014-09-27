class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        len_s=len(s)
        if len_s==0: return 0
        result=[0]*(len_s+1) #use dp and we need a vector
        result[0]=1
        if int(s[len_s-1])==0: result[1]=0
        else: result[1]=1 # initial values for dp
        for i in range(2,len_s+1):
            if s[len_s-i]=='0': result[i]=0
            else: #dominating one is not 0
                result[i]+=result[i-1]
                if int(s[len_s-i])*10+int(s[len_s-i+1])<=26:
                    result[i]+=result[i-2]
        return result[len_s]
