class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        if n==0: return
        if m==0:
            A[0:n]=B
            return
        ind_B=n-1
        ind_A=m-1
        ind_sort=m+n-1
        while ind_sort>=0:
            if ind_B<0:
                A[ind_sort]=A[ind_A]
                ind_A-=1
                ind_sort-=1
            elif ind_A<0:
                A[ind_sort]=B[ind_B]
                ind_B-=1
                ind_sort-=1
            else:
                if A[ind_A]>B[ind_B]:
                    A[ind_sort]=A[ind_A]
                    ind_sort-=1
                    ind_A-=1
                else:
                    A[ind_sort]=B[ind_B]
                    ind_sort-=1
                    ind_B-=1
        return
