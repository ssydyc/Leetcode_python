class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        #counting sort
        count=[0]*3
        for x in A:
            count[x]+=1 #count the number for each category
        temp_total=0
        for i in range(3):
            temp=count[i]
            count[i]=temp_total
            temp_total+=temp # record the place for each category
        for i in range(len(A)):
            if i<count[1]:
                A[i]=0
            elif i<count[2] and i>=count[1]:
                A[i]=1
            else:
                A[i]=2
        return
