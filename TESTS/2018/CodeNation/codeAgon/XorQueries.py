#!/bin/python

import math
import os
import random
import re
import sys

def solve(x, l, r):
    get_bin = lambda x, n: format(x,'b').zfill(n)
    m=max(x,l,r)
    ml=len(bin(m)[2:])
    xb=get_bin(x,ml)
    lb=get_bin(l,ml)
    rb=get_bin(r,ml)
    yb=""
    for i in range(ml):
        if xb[i]=='1':
            yb+='0'
        else:
            yb+='1'
        if yb<lb[:i+1]:
            yb=yb[:-1]+'1'
        elif yb>rb[:i+1]:
            yb=yb[:-1]+'0'
    return x^int(yb,2)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(raw_input().strip())
    for q_itr in xrange(q):
        xlr = raw_input().rstrip().split()
        x = int(xlr[0])
        l = int(xlr[1])
        r = int(xlr[2])
        result = solve(x, l, r)
        fptr.write(str(result) + '\n')
    fptr.close()
