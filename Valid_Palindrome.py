class Solution:
    # @param s, a string
    # @return a boolean
    
    def isPalindrome(self, s):
        if len(s)==0 or len(s)==1: return True
        start,end=0,len(s)-1
        while start<end:
            if not (s[start].isalpha() or s[start].isdigit()):
                start+=1
                continue
            elif not (s[end].isalpha() or s[end].isdigit()):
                end-=1
                continue
            else:
                temp1=s[start]
                temp2=s[end]
                if ord(s[start])<=ord('z') and ord(s[start])>=ord('a'): temp1=chr(ord(s[start])-32)
                if ord(s[end])<=ord('z') and ord(s[end])>=ord('a'): temp2=chr(ord(s[end])-32)
                if temp1==temp2:
                    start+=1
                    end-=1
                    continue
                else:
                    return False
        return True
