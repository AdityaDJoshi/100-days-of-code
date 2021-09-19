#define ll long long int
#define pb(x) push_back(x)
#define vi vector<int>
#include <bits/stdc++.h>
using namespace std;
string reverseInParentheses(string s)
{
    string ans = "";
    deque<char> d;
    int i = 0, ctr = 0;
    while (i < s.length())
    {
        if (s[i] != '(')
        {
            ans += s[i];
        }
        else
        {
            // ctr++;
            // i++;
            do
            {
                if (s[i] == '(')
                {
                    ctr++;
                }
                else if (s[i] == ')')
                {
                    ctr--;
                    /* code */
                }
                else
                {
                    d.push_back(s[i]);
                }
                i++;
                /* code */
            } while (ctr != 0 && i < s.length());

            while (!d.empty())
            {
                ans += d.back();
                d.pop_back();
            }
            i--;
        }

        i++;
    }
    return ans;
}
int main(void)
{

    string s = "foo(bar)baz";
    s = "foo(bar(baz))blim";
    cout << reverseInParentheses(s);
}