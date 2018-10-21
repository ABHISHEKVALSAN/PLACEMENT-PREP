vector<vector<int> > Solution::generateMatrix(int A) {
    int mat[A][A],r,r1,r2,c,c1,c2,lr,ud,i;
    vector<int> v(A,0);
    vector<vector <int>> MAT(A,v);
    r1=0;
    r2=A-1;
    c1=0;
    c2=A-1;
    i=0;
    r=0;
    c=0;
    lr=1;
    ud=0;
    while(r1<=r2 && c1<=c2){
        MAT[r][c]=++i;
        if(lr==1){
            if(c==c2){
                r++;
                r1++;
                lr=0;
                ud=1;
            }
            else
                c++;
        }
        else if (lr==-1){
            if (c==c1){
                r--;
                r2--;
                lr=0;
                ud=-1;
            }
            else
                c--;

        }
        else if(ud==1){
            if(r==r2){
                c--;
                c2--;
                ud=0;
                lr=-1;
            }
            else
                r++;

        }
        else if(ud==-1){
            if(r==r1){
                c++;
                c1++;
                ud=0;
                lr=1;
            }
            else
                r--;
        }
    }
    return MAT;
}
