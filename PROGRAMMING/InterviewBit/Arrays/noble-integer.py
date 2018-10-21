class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        if A[-1]==0:
            return 1
        for i in range(len(A)-1):
            if A[i]!=A[i+1] and A[i]==len(A)-i-1:
                return 1
        return -1
