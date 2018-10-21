class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        ans=[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
        if A<5:
            return ans[A]
        for i in range(A-4):
            ans.append([])
            ans[-1].append(1)
            for j in range(len(ans[-2])-1):
                ans[-1].append(ans[-2][j]+ans[-2][j+1])
            ans[-1].append(1)
        return ans[A]
