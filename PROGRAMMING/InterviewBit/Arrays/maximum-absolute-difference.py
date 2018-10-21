class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        a1=[]
        a2=[]
        for i in range(len(A)):
            a1.append(A[i]+(i+1))
            a2.append(A[i]-(i+1))
        a=a1+a2
        return max(max(a1)-min(a1),max(a2)-min(a2))

#Tip1   :   Modulo always has a shortcut
#Note1  :   Took more than 1 hour to solve
