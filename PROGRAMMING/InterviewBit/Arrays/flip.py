class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        A=map(int,A)
        if sum(A)==len(A):
            return []
        s=0
        ms=0
        L=1
        R=1
        mL=1
        mR=0
        for i in A:
            if i==0:
                s+=1
                if s>ms:
                    mL=L
                    mR=R
                    ms=s
                R+=1
            elif i==1:
                s-=1
                if s<0:
                    s=0
                    R+=1
                    L=R
                else:
                    R+=1
        return [mL,mR]
