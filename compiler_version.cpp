// https://www.hackerearth.com/practice/algorithms/string-algorithm/basics-of-string-manipulation/practice-problems/algorithm/compiler-version-2/
#include <bits/stdc++.h>

using namespace std;
int main(void)
{
    string line;
    char x;

    while (getline(cin, line))
    {
        string temp = "";
        for (int i = 0; i < line.length(); i++)
        {
            x = line[i];
            if (x == '/' && line[i + 1] == '/')
            {
                while (i < line.length())
                {

                    x = line[i];
                    temp += x;
                    i++;
                }
                continue;
            }
            else if (x == '-' && line[i + 1] == '>')
            {
                temp += '.';
                i++;
            }
            else
            {
                temp += x;
            }
        }
        cout << temp << endl;
    }
}