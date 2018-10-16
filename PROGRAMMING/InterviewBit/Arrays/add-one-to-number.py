class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        s="".join(map(str,A))
        I=int(s)+1
        ans=map(int,list(str(I)))
        return ans

