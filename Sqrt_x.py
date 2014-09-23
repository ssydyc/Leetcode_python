
class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        x_prev=x
        if x_prev==0: return 0
        x_cur=0.5*x_prev+x/(2.0*x_prev)
        while abs(x_prev-x_cur)>0.1:
            x_prev=x_cur
            if x_prev==0: return 0
            x_cur=0.5*x_prev+x/(2.0*x_prev)
        return int(x_cur)
