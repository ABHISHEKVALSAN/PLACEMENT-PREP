#include <bits/stdc++.h>
using namespace std;
int findSum(int A[], int B[], int n1,int n2)
{
    unordered_map<int, int> hash;
    for (int i = 0; i < n1; i++)
        hash[A[i]]++;
    for (int i = 0; i < n2; i++)
        hash[B[i]]++;
    int sum = 0;
    for (auto x: hash)
        if (x.second == 1)
            sum += x.first;
    return sum;
}
int main()
{
    int A[] = { 5, 4, 9, 2, 3 };
    int B[] = { 2, 8, 7, 6, 3 };
    int n1 = sizeof(A) / sizeof(A[0]);
    int n2 = sizeof(B) / sizeof(B[0])
    cout << findSum(A, B, n1, n2);
    return 0;
}
