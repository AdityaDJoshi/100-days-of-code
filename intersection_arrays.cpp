#define ll long long int
#define pb(x) push_back(x)
#define vi vector<int>
#include <bits/stdc++.h>
using namespace std;
int gcd(int a, int b)
{
    if (b == 0)
        return a;
    a %= b;
    return gcd(b, a);
}
bool PALIN(string s)
{
    ll i = 0;
    ll j = s.length() - 1;
    while (i <= j)
    {
        if (s[i] != s[j])
            return false;
        j--;
        i++;
    }
    return true;
}
int main(void)
{
    vi v1 = {4, 9, 5},
       v2 = {9, 4, 9, 8, 4};
    map<int, int> m1, m2;
    for (auto x : v1)
    {
        m1[x]++;
        /* code */
    }
    for (auto x : v2)
    {
        m2[x]++;
        /* code */
    }
    vi v3;
    for (auto x : m1)
    {
        for (int j = 0; j < (min(m1[x.first], m2[x.first])); j++)
        {
            /* code */
            v3.push_back(x.first);
        }

        /* code */
    }
    for (auto x : v3)
    {
        cout << x << " ";
    }
}