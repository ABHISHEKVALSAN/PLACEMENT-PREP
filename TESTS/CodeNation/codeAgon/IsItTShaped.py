#!/bin/python

import math
import os
import random
import re
import sys

def solve(grid):
    x=[]
    y=[]
    grid.sort()
    xmin=grid[0][0]
    ymin=grid[0][1]
    for i in grid:
        if i[1]<ymin:
            ymin=i[1]
    c=[]
    for i in grid:
        c=c+[i[0]-xmin]+[i[1]-ymin]
    c1=[0,0,0,1,0,2,1,1,2,1]
    c2=[0,2,1,0,1,1,1,2,2,2]
    c3=[0,0,1,0,1,1,1,2,2,0]
    c4=[0,1,1,1,2,0,2,1,2,2]
    if c==c1 or c==c2 or c==c3 or c==c4:
        return "Yes"
    return "No"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(raw_input().strip())
    for t_itr in xrange(t):
        points = []
        for _ in xrange(5):
            points.append(map(int, raw_input().rstrip().split()))
        result = solve(points)
        fptr.write(result + '\n')
    fptr.close()
