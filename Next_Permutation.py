'''
Created on Jan 20, 2014

@author: songsi
'''
class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        change=-1
        if len(num)==0 or len(num)==1:
            return num
        for i in range(len(num)-1,0,-1):
            j=i-1
            if num[j]<num[i]:
                change=j
            if change!=-1: break
        #now we need to sort all after digits j
        for i in range(change+1,len(num)-1):
            for j in range(i+1,len(num)):
                if num[i]>num[j]:
                    temp=num[i]
                    num[i]=num[j]
                    num[j]=temp
                                       
        if change==-1: return num
        for i in range(change+1,len(num)):
            if num[i]>num[change]:
                temp=num[i]
                num[i]=num[change]
                num[change]=temp
                break
        return num
    
test=Solution()
print test.nextPermutation([1,2,3])