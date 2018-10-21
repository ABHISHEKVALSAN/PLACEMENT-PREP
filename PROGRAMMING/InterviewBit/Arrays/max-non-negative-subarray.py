class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        ans=[]
        temp=[]
        for i in A:
            if i>=0:
               temp.append(i)
            else:
                temp=[]
            if sum(temp)>sum(ans):
                ans=temp
            elif sum(temp)==sum(ans):
                if len(temp)>len(ans):
                    ans=temp

        return ans
