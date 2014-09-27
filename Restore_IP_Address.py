class Solution:
    # @param s, a string
    # @return a list of strings
    def isvalid(self,s):
        if s[0]=='0' and len(s)>1: return True
        if int(s)>255: return True
        return False
        
    def restoreIpAddresses(self, s):
        n=len(s)
        result=[]
        result_IP=[]
        for i in range(1,4):
            for j in range(1,4):
                for m in range(1,4):
                    for k in range(1,4):
                        if i+j+m+k==n: result.append((i,j,m,k))
        for temp in result:
            if self.isvalid(s[0:temp[0]]) or self.isvalid(s[temp[0]:temp[0]+temp[1]]) or self.isvalid(s[sum(temp[0:2]):sum(temp[0:3])]) or self.isvalid(s[sum(temp[0:3]):sum(temp[0:4])]): continue
            temp_IP=s[0:temp[0]]+'.'+s[temp[0]:temp[0]+temp[1]]+'.'+s[sum(temp[0:2]):sum(temp[0:3])]+'.'+s[sum(temp[0:3]):sum(temp[0:4])]
            result_IP.append(temp_IP)
        return result_IP
