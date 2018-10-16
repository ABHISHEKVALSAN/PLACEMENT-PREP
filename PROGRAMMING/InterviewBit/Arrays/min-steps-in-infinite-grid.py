class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        i=0
        jumps=0
        if len(A)==1:
            return 0
        while i<len(A)-1:
            jumps+=max(abs(A[i+1]-A[i]),abs(B[i+1]-B[i]))
            i+=1
        return jumps

# What if order is not given? What is the minimum distance then?
