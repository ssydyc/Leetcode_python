class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of string
    
    def fullJustify(self, words, L):
        result=[]
        candid=[]
        cur_L=0
        for temp in words:
            if candid==[]:
                candid.append(temp)
                cur_L+=len(temp)
            else:
                if cur_L+1+len(temp)>L: #we can't hold another word in this line
                    #now it's time to pour candid into result
                    if len(candid)==1:
                        temp_line=candid[0]+' '*(L-len(candid[0]))
                    else:
                        num_space=(L-cur_L)/(len(candid)-1)
                        left_add=(L-cur_L)%(len(candid)-1) # decide the number of left words having additional space
                        temp_line=candid[0]
                        for i in range(1,len(candid)):
                            if left_add>0:
                                left_add-=1
                                temp_line+=' '*(num_space+2)+candid[i]
                            else:
                                temp_line+=' '*(num_space+1)+candid[i]
                    result.append(temp_line)
                    #now start over again
                    candid=[temp]
                    cur_L=len(temp)
                else:
                    candid.append(temp)
                    cur_L+=len(temp)+1
        if candid==[]: return [] #nothing left
        else:
            temp_line=candid[0]
            for i in range(1,len(candid)):
                temp_line+=' '+candid[i]
            temp_line+=' '*(L-cur_L)
            result.append(temp_line)     
        return result
