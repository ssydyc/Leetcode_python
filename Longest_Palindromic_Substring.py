class Solution:
    # @return a string
    def longestPalindrome(self, s):
        max_size=1
        max_start=0
        max_end=0 #initilize the value
        if not s: return ""
        for i in range(len(s)):
            start,end=i-1,i+1 #middle one is an extra
            max_cur=1 # for current test
            while start>=0 and end<len(s): # no need to stop
                if s[start]==s[end]:
                    max_cur+=2
                    start-=1
                    end+=1
                else:
                    break
            if max_cur>max_size:
                max_size=max_cur
                max_start=start+1
                max_end=end-1
                
            start,end=i,i+1 # no middle one
            max_cur=0
            while start>=0 and end<len(s): # no need to stop
                if s[start]==s[end]:
                    max_cur+=2
                    start-=1
                    end+=1
                else:
                    break
            if max_cur>max_size:
                max_size=max_cur
                max_start=start+1
                max_end=end-1
        return s[max_start:max_end+1]
        
