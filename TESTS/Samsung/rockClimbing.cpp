#include<iostream>
using namespace std;
void printMat(int a[1000][1000],int n,int m){
  int i,j;
  cout<<"\n\n";
  for(i=1;i<=n;i++){
    for(j=1;j<=m;j++){
      cout<<a[i][j]<<" ";
    }
    cout<<endl;
  }
}
int traverse(int a[1000][1000],int n,int m,int i,int j,int h){
  int ans,k;
  printMat(a,n,m);
  //cout<<i<<" "<<j;
  if(i<=0 or j<=0 or i>n or j>m)
    return -1;
  if(a[i][j]==1 or a[i][j]==3){
    //for avoiding cycles during traversal,
    //equivalent to marking as visited
    a[i][j]*=-1;

    //moving left in matrix
    cout<<"left";
    ans=traverse(a,n,m,i,j-1,h);
    if(ans>=1){
        return ans;
    }

    //moving down in matrix
    cout<<"down";
    for(k=1;k<=h;k++){
      ans=traverse(a,n,m,i+k,j,h);
      if(ans>=1){
        return ans;
      }
    }

    //moving right in matrix
    cout<<"right";
    ans=traverse(a,n,m,i,j+1,h);
    if(ans>=1){
        return ans;
    }

    //moving up in matrix
    cout<<"up";
    for(k=1;k<=h;k++){
      ans=traverse(a,n,m,i-k,j,h);
      if(ans>=1){
        return ans;
      }
    }
    // restoring initial value after backtracking
    a[i][j]*=-1;
    return ans;
  }
  else if (a[i][j]<=0){
    return -1;
  }
  else if(a[i][j]==2)
    return h;
  else
    return -1;
}
int main(){
  
  //di,dj is the destination indices
  //h is the height for the jump or the difficulty
  int i,j,di,dj,t,T,test_cases,n,m,h,ans=-1;
  int a[1000][1000];
  cout<<"Enter no of testcases \n";
  cin>>T;
  for(t=1;t<=T;t++){
    cout<<" Enter dimensions  \n";
    cin>>n>>m;
    h=n-1;
    cout<<" Enter Elements \n";
    for(i=1;i<=n;i++)
      for(j=1;j<=m;j++){
        cin>>a[i][j];
        if(a[i][j]==3){
          di=i;
          dj=j;
        }
      }
    for(i=1;i<=h;i++){
        ans=traverse(a,n,m,di,dj,i);
        if(ans>=1)
          break;
    }
    cout<<"#"<<t<<" "<<ans<<endl;
  }
  return 0;
}
