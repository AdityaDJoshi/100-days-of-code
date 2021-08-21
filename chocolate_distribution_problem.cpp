// https://practice.geeksforgeeks.org/problems/chocolate-distribution-problem3825/1
#define ll long long int
#define pb(x) push_back(x)
#define vi vector<int>
#include <bits/stdc++.h>
using namespace std;

long long findMinDiff(vector<long long> a, long long n, long long m)
{
    //code
    sort(a.begin(), a.end());
    long long int d = 99999999;
    for (int i = 0; i <= n - m; i++)
    {
        // cout<<a[i]<<" "<<a[i+m]<<endl;
        d = min(d, a[i + m - 1] - a[i]);
    }
    return d;
}
int main(void)
{
}