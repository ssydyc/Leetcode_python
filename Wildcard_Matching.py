class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        s_len=len(s)
        p_len=len(p) # record the length
        s_current=0
        p_current=0
        s_last=0
        p_last=-1 #backtracking
        while s_current<s_len: #don't stop util to the end
            if p_current<p_len and (s[s_current]==p[p_current] or p[p_current]=='?'):
                p_current+=1
                s_current+=1
            elif p_current<p_len and p[p_current]=='*':
                s_last=s_current
                p_last=p_current
                p_current+=1    #record the last * place
            elif p_last!=-1: # we have * before
                s_last+=1
                s_current=s_last
                p_current=p_last
            else:
                return False
        while p_current<p_len and p[p_current]=='*':
            p_current+=1
        if p_current==p_len:
            return True
        else:
            return False
                
            
