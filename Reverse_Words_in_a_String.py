class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        if len(s)==0: # case that no element exsits
            return ""
        sep_string=s.split(" ")
        result=[]
        for i in range(len(sep_string)-1,-1,-1):
            if sep_string[i]!='':
                result.append(sep_string[i])
        return ' '.join(result)
