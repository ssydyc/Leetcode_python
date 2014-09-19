class Solution:
    # @return an integer
    def totalNQueens(self, n):
        if n==0: return 0
        current_level=0
        sum_list=[]
        substract_list=[]
        current_list=[-1]*n
        results=0
        return self.my_solve(n,current_level,sum_list,substract_list,current_list,results) #current list is the list we have now
        
    def my_solve(self,n,current_level,sum_list,substract_list,current_list,results):
        while current_level>=0: #we have finished iterating all levels
            if current_list[current_level]==n-1: # we can't add in this level
                current_list[current_level]=-1 #start the level from the beginning
                current_level-=1
                if current_level!=-1:
                    sum_list.pop()
                    substract_list.pop() #go to previous level
                continue
            if (current_list[current_level]+1 not in current_list) and (current_list[current_level]+1-current_level not in substract_list) and (current_list[current_level]+current_level+1 not in sum_list): #this is the case that we need to add cases
                if current_level!=n-1: #go to next level
                    current_list[current_level]+=1
                    substract_list.append(current_list[current_level]-current_level)
                    sum_list.append(current_list[current_level]+current_level)
                    current_level+=1
                    continue
                else: #now it's true
                    current_list[current_level]+=1
                    results+=1
                    continue
            current_list[current_level]+=1
            continue
        return results
