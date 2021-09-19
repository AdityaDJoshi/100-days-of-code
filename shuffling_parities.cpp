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
template <typename T>
std::ostream &operator<<(std::ostream &os, const std::vector<T> &vec)
{
    for (auto elem : vec)
    {
        os << elem << " ";
    }
    return os;
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
    cin.tie(NULL);
    cout.tie(NULL);
    ios_base::sync_with_stdio(false);

    long long int t = 1;
    cin >> t;
    while (t--)
    {
        ll n, x;
        cin >> n;
        vector<ll> v;

        ll eveninds = n / 2, evennos = 0;
        for (ll i = 0; i < n; i++)
        {
            cin >> x;
            if (x % 2 == 0)
                evennos++;
            v.push_back(x);
        }

        cout << min(evennos, (n - eveninds)) + min((n - evennos), eveninds) << endl;

        //enter code here
    }
}