class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if len(s1)+len(s2)!=len(s3): return False
        if s1=='':
            return s2==s3
        if s2=='':
            return s1==s3
        #now we have all non-empty set
        pre=[False]*(len(s1)+1)
        cur=[False]*(len(s1)+1)
        for i in range(len(s2)+1):
            cur=[False]*(len(s1)+1)
            for j in range(len(s1)+1):
                if i==0: #first line
                    if j==0: cur[j]=True
                    else:
                        if cur[j-1]==True and s1[j-1]==s3[j-1]:
                            cur[j]=True
                else:
                    if pre[j]==True and s2[i-1]==s3[i+j-1]:
                        cur[j]=True
                    if j>0:
                        if cur[j-1]==True and s1[j-1]==s3[i+j-1]:
                            cur[j]=True
            pre,cur=cur,pre
        return pre[len(s1)]
