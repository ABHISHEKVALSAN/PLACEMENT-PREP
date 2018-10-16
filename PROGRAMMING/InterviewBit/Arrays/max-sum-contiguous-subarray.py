class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        ms=max(A)
        i=0
        f=1
        for i in A:
            if i>=0:
                f=0
                break
        if f:
            return ms
        s=0
        for i in A:
            s+=i
            if s<0:
                s=0
            if s>ms:
                ms=s
        return ms

#Tip 1: If all numbers in a list is negative, then it has to be handled separatly 
