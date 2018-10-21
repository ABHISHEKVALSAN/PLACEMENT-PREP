class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        n=len(A)
        ans=[]
        for i in range(n):
            for j in range(n):
                try:
                    ans[i+j].append(A[i][j])
                except:
                    ans.append([])
                    ans[i+j].append(A[i][j])
        return ans
