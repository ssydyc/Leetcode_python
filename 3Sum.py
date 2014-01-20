'''
Created on Jan 20, 2014

@author: songsi
'''

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        answer=set([])
        for i in range(0,len(num)-2):
            #num[i] will be the first element
            target=0-num[i]
            head=i+1
            tail=len(num)-1
            while(tail>head):
                if num[head]+num[tail]==target:
                    answer=answer|set([(num[i],num[head],num[tail])])
                    tail-=1
                    head+=1
                elif num[head]+num[tail]>target:
                    tail-=1
                else:
                    head+=1
        result=[]
        for temp in answer:
            result.append(list(temp))
        return result
        
test=Solution()
print test.threeSum([-1,0,1,2,-1,-4])