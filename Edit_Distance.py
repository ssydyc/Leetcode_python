class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        #word1 to word2
        len_1=len(word1)
        len_2=len(word2)
        prev_row=[i for i in range(len_2+1)] #add another element for starting point
        cur_row=[0]*(len_2+1)
        for i in range(len_1):
            for j in range(len_2+1): #notice the index here should plus one
                if j==0: cur_row[j]=i+1
                else:
                    if word1[i]==word2[j-1]: 
                        cur_row[j]=prev_row[j-1]
                    else:
                        cur_row[j]=min(cur_row[j-1]+1,prev_row[j]+1,prev_row[j-1]+1)
            prev_row, cur_row=cur_row,prev_row
        return prev_row[len_2]
