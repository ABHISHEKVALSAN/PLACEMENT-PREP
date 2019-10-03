#include<bitset>
#include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
  		int n;
    	cin>>n;
    	int d,mcount=0;
      int count=0;
    	while(n>0)
    	{
    	   d=n%2;
         n/=2;
         if(d==0){
           count=0;
         }
         else{
           count++;
           if(count>mcount){
             mcount=count;
           }
         }
    	}
    	cout<<mcount<<endl;
	}
	return 0;
}
