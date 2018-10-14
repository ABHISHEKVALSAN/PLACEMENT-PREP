#include<iostream>
using namespace std;

int traverse(int arr[20][20],int n,int bin[20],int bl,int i,int j,int curInd,int curAns){
  if(i<0 or j<0 or i>=n or j>=n or arr[i][j]<0 or arr[i][j]!=bin[curInd])
    return curAns;
  if(bin[curInd]==arr[i][j]){
    if(curInd==bl-1){
      return curAns+1;
    }
    else{
      arr[i][j]-=2;
      curAns=traverse(arr,n,bin,bl,i+1,j,curInd+1,curAns);
      curAns=traverse(arr,n,bin,bl,i-1,j,curInd+1,curAns);
      curAns=traverse(arr,n,bin,bl,i,j+1,curInd+1,curAns);
      curAns=traverse(arr,n,bin,bl,i,j-1,curInd+1,curAns);
      arr[i][j]+=2;
      return curAns;
    }
  }
  return curAns;
}
void printAr(int arr[20],int n){

    int i;
    cout<<endl;
    for(i=0;i<n;i++)
      cout<<arr[i]<<" ";
    cout<<endl;
}
void printMat(int a[20][20],int n){
  int i,j;
  cout<<endl;
  for(i=0;i<n;i++){
    for(j=0;j<n;j++){
      cout<<a[i][j]<<" ";
    }
    cout<<endl;
  }
}
int main(){  

  int i,j,t,T,temp,n,num,ans;
  int arr[20][20],bin[20],bl=0;
  

  cout<<"Enter no of testcases \n";
  cin>>T;
  
  for(t=1;t<=T;t++){
    
    ans=0;
    cout<<" Enter Dimension and the Number  \n";
    cin>>n>>num;

    cout<<" Enter Elements \n";
    for(i=0;i<n;i++)
      for(j=0;j<n;j++)
        cin>>arr[i][j];
    
    

    bl=0;
    while(num>0){
      bin[bl++]=num%2;
      num/=2;
    }
    //bl is now the length of the binary number

    //reversing the array, so that it's binary equivalent of num
    int symmetry=2;
    for(i=0;i<bl/2;i++){
      if(bin[i]!=bin[bl-i-1])
        symmetry=1;
      temp=bin[i];
      bin[i]=bin[bl-i-1];
      bin[bl-i-1]=temp;
    }

    //printMat(arr,n);
    //printAr(bin,bl);
    for(i=0;i<n;i++)
      for(j=0;j<n;j++)
        ans+=traverse(arr,n,bin,bl,i,j,0,0);
    cout<<"#"<<t<<" "<<ans/symmetry<<endl;
    }
  return 0;
}
