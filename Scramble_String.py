class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        if len(s1)!=len(s2): return False
        if len(s1)==0: return True
        temp1,temp2=list(s1),list(s2)
        temp1.sort()
        temp2.sort()
        if temp1!=temp2: 
            return False
        result=[[[False for i in range(len(s1))] for j in range(len(s1))] for k in range(len(s1))] # 3 dimensional DP
        for k in range(len(s1)):
            for i in range(len(s2)-k):
                for j in range(len(s1)-k):
                    #s[i][j][k] means that starting from i and j, i....(i+k) will be scrambling of j....(j+k)
                    if k==0:
                        if s1[i]==s2[j]:
                            result[i][j][k]=True
                        else:
                            result[i][j][k]=False
                    else:
                        if s1[i:i+k+1]==s2[j:j+k+1]:
                            result[i][j][k]=True
                            continue
                        for m in range(k): #
                            if result[i][j][m] and result[i+m+1][j+m+1][k-m-1]:
                                result[i][j][k]=True
                                break
                            if result[i][j+k-m][m] and result[i+m+1][j][k-m-1]:
                                result[i][j][k]=True
                                break
        return result[0][0][len(s1)-1]
            
