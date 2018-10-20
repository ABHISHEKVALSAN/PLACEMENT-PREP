#include<bits/stdc++.h>
using namespace std;
int main(){
	int T,i,n,flag;
	string str;
	cin>>T;
	while(T--){
		cin>>str;
		n = str[str.size()-1]-'0';
    str[str.size()-1]='0';
		if(n<5)
			cout<<str<<endl;
		else{
			i=str.size()-2;
			while(i>=0){
				if(str[i]=='9'){
					str[i]='0';
				}
				else{
					str[i]=str[i]+1;
					break;;
				}
				i--;
			}
			if(i==-1)
        cout<<1<<str<<endl;
			else
        cout<<str<<endl;
		}
	}
}
