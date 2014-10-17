class Solution:
    # @param tokens, a list of string
    # @return an integer
    def operator(self,num1,num2,opt):
        if opt=='+':
            return num1+num2
        elif opt=='-':
            return num2-num1
        elif opt=='*':
            return num1*num2
        else:
            if num2*num1<0:
                return -((-num2)/num1)
            else:
                return num2/num1
    
    def evalRPN(self, tokens):
        stack=[]
        if not tokens: return 0
        for (i,v) in enumerate(tokens):
            try:
                temp=int(v)
                stack.append(temp)
            except: #we can't convert v
                num1=stack.pop()
                num2=stack.pop()
                stack.append(self.operator(num1,num2,v))
        return stack[0]
