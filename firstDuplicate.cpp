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
int firstDuplicate(vector<int> a)
{
    map<int, bool> doesRepeat;
    map<int, int> counter;
    vector<int> copy = a;
    sort(copy.begin(), copy.end());

    for (int i = 0; i < a.size(); i++)
    {
        if (counter[a[i]] > 0)
            return a[i];
        // cout << counter[a[i]] << "\n";
        counter[a[i]] += 1;
    }
    return -1;
}
int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    ios_base::sync_with_stdio(false);

    vector<int> v = {2,
                     1,
                     3,
                     5,
                     3,
                     2};
    v = {2, 4, 3, 5, 1};
    cout << firstDuplicate(v);
}