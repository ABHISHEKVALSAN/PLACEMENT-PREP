class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n=len(A)
        amb=0
        a2mb2=0
        for i in range(n):
            amb+=A[i]-(i+1)
        for i in range(n):
            a2mb2+=A[i]**2-(i+1)**2
        apb=a2mb2//amb
        a=(apb+amb)/2
        b=(apb-amb)/2
        return [a,b]

#Tip 1  :   Find the sum of difference of Actual and Given simultaneously,
#       :   to avoid overflow   
