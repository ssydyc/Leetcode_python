class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        if len(T)==0: return 1 # only one empty subsequence
        if len(T)>len(S): return 0
        prev=[1]*len(S)
        cur=[0]*len(S)
        for i in range(len(T)):
            for j in range(len(S)):
                if j==0 and i==0 and T[i]==S[j]:
                    cur[j]=1
                if j>0:
                    cur[j]+=cur[j-1]
                    if T[i]==S[j]: cur[j]+=prev[j-1] # add another case
            prev,cur=cur,prev
            cur=[0]*len(S)
        return prev[len(S)-1]
