#include <bits/stdc++.h>
using namespace std;
int findSum(int A[], int B[], int n1,int n2)
{
    unordered_map<int,array<int,2>> hash;
    int sum=0;
    for (int i = 0; i < n1; i++){
        hash[A[i]][0]++;
    }
    for (int i = 0; i < n2; i++){
        hash[B[i]][1]++;
    }
    for (auto x:hash){
      if(x.second[0]*x.second[1]==0){
        sum+=x.first*(x.second[0]+x.second[1]);
      }
    }
    return sum;
}
int main()
{
    int A[] = { 1, 2, 2, 3, 5};
    int B[] = { 3, 4, 5, 5 };
    int n1 = sizeof(A) / sizeof(A[0]);
    int n2 = sizeof(B) / sizeof(B[0]);
    cout << findSum(A, B, n1, n2);
    return 0;
}
