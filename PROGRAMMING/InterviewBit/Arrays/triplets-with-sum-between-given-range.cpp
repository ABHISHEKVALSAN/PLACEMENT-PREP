int Solution::solve(vector<string> &A) {

    int n=A.size(),i;
    vector<double> x,y,z;
    vector<double> x1,x2;
    for(i=0;i<n;i++){
        double ele=stod(A[i]);
        if( ele <= (2.0/3.0)){
            x.push_back(ele);
        }
        if(ele>2.0/3.0 && ele <=1){
            y.push_back(ele);
        }
        if(ele>1 and ele<2){
           z.push_back(ele);
        }
    }
    int xn,yn,zn;
    xn=x.size();
    yn=y.size();
    zn=z.size();
    sort(x.begin(),x.end());
    sort(y.begin(),y.end());
    sort(z.begin(),z.end());
    if(xn>=3){
        //cout<<"x3";
        if(x[xn-1]+x[xn-2]+x[xn-3]>1)
            return 1;
    }
    if(zn>=1 && xn>=2){
        //cout<<"x2z1";
        if(z[0]+x[0]+x[1]<2)
            return 1;
    }
    if(zn>=1 && yn>=1 && xn>=1 ){
        //cout<<"x1y1z1";
        if(z[0]+y[0]+x[0]<2)
            return 1;
    }
    if(xn>=1&&yn>=2){
        //cout<<"x1y2";
        if(y[0]+y[1]+x[0]<2)
            return 1;
    }
    if(xn>=2 && yn>=1)
    {
      //cout<<"x2y1";
      for(i=0;i<xn;i++){
          if(x[i]<0.5)
            x1.push_back(x[i]);
          else
            x2.push_back(x[i]);
      }
      int x1n=x1.size(),x2n=x2.size();
      if(x2n>=2){
          //cout<<"x22";
        if(x2[0]+x2[1]+y[0]<2)
            return 1;
      }
      if(x1n>=2){
          //cout<<"x12";
          if(x1[x1n-1]+x1[x1n-2]+y[yn-1]>1){
            //cout<<"\n"<<x1[x1n-1]<<" "<<x1[x1n-2]<<" "<<y[yn-1];
            return 1;}
      }
      if(x1n>=1 && x2n>=1){
          //cout<<"x11x21";
          if(x1[0]+x2[0]+y[0]<2)
            return 1;
      }
    }
    return 0;
}
//Tip1  : Handling boundary cases should be neat
//Note 1: Took more than 1 hour to solve 
