class Solution:
    # @param s, a string
    # @return a boolean
    def digit_valid(self,s):
        if s.isdigit() or s=='e' or s=='.' or s=='+' or s=='-':
            return True
        else:
            return False
            
    def is_all_digit(self,s):
        for temp in s:
            if not temp.isdigit(): return False
        return True
        
    def isNumber(self, s):
        s=s.strip(' ') #take ' ' off
        e_exist=False #record
        dot_exist=False
        e_place=0 #record place of e
        dot_place=0
        for i in range(len(s)):
            if not self.digit_valid(s[i]): return False
            if e_exist and s[i]=='e': return False #too many e
            if s[i]=='e':
                e_place=i
                e_exist=True
            if e_exist and s[i]=='.': return False #no . after e
            if s[i]=='.':
                dot_place=i
                dot_exist=True
        if not dot_exist and not e_exist:
            if s=='': return False
            else:
                if (s[0]=='+' or s[0]=='-' or s[0].isdigit()) and self.is_all_digit(s[1:]): return True
                else: return False
        if not e_exist:
            s1=s[0:dot_place]
            s2=s[dot_place+1:]
            if (s1=='' or s1=='+' or s1=='-') and s2=='': return False
            if (s1=='' or s1[0]=='+' or s1[0]=='-' or s1[0].isdigit()) and self.is_all_digit(s1[1:]) and self.is_all_digit(s2):
                return True
            else:
                return False
        if not dot_exist: #dot doesn't exist
            s1=s[0:e_place]
            s2=s[e_place+1:]
            if (s1=='' or s1=='-' or s1=='+') or s2=='': return False
            if (s1[0]=='+' or s1[0]=='-' or s1[0].isdigit()) and self.is_all_digit(s1[1:]) and (((s2[0]=='+' or s2[0]=='-') and len(s2)!=1) or s2[0].isdigit()) and self.is_all_digit(s2[1:]):
                return True
            else:
                return False
        #the last part
            
        s1=s[0:dot_place]
        s2=s[dot_place+1:e_place]
        s3=s[e_place+1:] #seperate into three parts
        if (s1=='' and s2=='') or s3=='': return False
        if (s1=='' or s1[0]=='+' or s1[0]=='-' or s1[0].isdigit()) and self.is_all_digit(s1[1:]) and self.is_all_digit(s2) and (((s3[0]=='+' or s3[0]=='-') and len(s3)!=1) or s3[0].isdigit()) and self.is_all_digit(s3[1:]):
            return True
        else:
            return False
        
        
