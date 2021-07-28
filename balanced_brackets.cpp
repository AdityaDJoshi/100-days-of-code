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
    // cin >> t;
    while (t--)
    {
        stack<char> stack;
        string s;
        bool flag = true;
        cout << stack.top();
        // getline(cin, s);
        for (auto x : s)
        {
            if (x == '(' || x == '{' || x == '[')
            {
                stack.push(x);
                continue;
            }
            if (stack.size() == 0)
            {
                flag = false;
                break;
            }

            else if (x == ')')
            {
                if ((stack.top() == '('))
                {
                    stack.pop();
                }
                else
                {
                    flag = false;
                    break;
                }
            }

            else if (x == '}')
            {
                if ((stack.top() == '{'))
                {
                    stack.pop();
                }
                else
                {
                    flag = false;
                    break;
                }
            }

            else if (x == ']')
            {
                if ((stack.top() == '['))
                {
                    stack.pop();
                }
                else
                {
                    flag = false;
                    break;
                }
                /* code */
            }
        }
        if ((stack.size() == 0) && (flag))
        {
            cout << "YES";
        }
        else
        {
            cout << "NO";
        }
        //enter code here
    }
}