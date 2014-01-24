'''
Created on Jan 22, 2014

@author: songsi
'''
class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        if len(num)<4: return []
        num.sort()
        Sum_2={}
        repeat={}
        answer=[]
        for i in range(0,len(num)):
            if num[i] in repeat: 
                repeat[num[i]]+=1
            else:
                repeat[num[i]]=1
                    
        for i in range(0,len(num)-1):
            for j in range(i+1,len(num)):
                if num[i]+num[j] in Sum_2:
                    Sum_2[num[i]+num[j]].append((num[i],num[j]))
                else:
                    Sum_2[num[i]+num[j]]=[(num[i],num[j])]
            
        for i in range(0,len(num)-1):
            for j in range(i+1,len(num)):
                target_2=target-num[i]-num[j]
                if target_2 in Sum_2:
                    for temp_tuple in Sum_2[target_2]:
                        if temp_tuple[0]>=num[j]:
                            count=self.mycount(num[i], num[j], temp_tuple[0], temp_tuple[1])
                            noproblem=True
                            mynum=[num[i], num[j], temp_tuple[0], temp_tuple[1]]
                            for count1 in range(0,4):
                                if repeat[mynum[count1]]<count[count1]:
                                    noproblem=False
                            if noproblem:
                                answer.append((num[i], num[j], temp_tuple[0], temp_tuple[1]))
                            
        answer=set(answer)
        result=[]
        for temp in answer:
            result.append(list(temp))
        return result
    
    def mycount(self,i,j,m,n):
        mynum=[i,j,m,n]
        count=[]
        for num1 in mynum:
            temp=0
            for num2 in mynum:
                if num1==num2:
                    temp+=1
            count.append(temp)
        return count
        
        
        
        
             
test=Solution()
print test.fourSum([-3,-1,0,2,4,5], 0)