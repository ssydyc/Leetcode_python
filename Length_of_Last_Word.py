class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        end_word=-1
        begin_word=-1
        s_len=len(s)
        for i in range(s_len):
            if i<s_len-1 and s[i]==' ' and s[i+1]!=' ':
                begin_word=i
            if (s[i]!=' ') and (i==s_len-1 or s[i+1]==' '):
                end_word=i
        return end_word-begin_word
