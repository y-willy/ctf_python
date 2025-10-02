#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string word = "EDVLF FUBSWR GUHDPKDFN";
    int len = 23;


    for (int shift = 1; shift <= 26; shift++)
    {
        string crypto_char = "";
        for (char c : word)
        {
            if (c >= 'A' && c <= 'Z')
            {
                c = 'A' + (c - 'A' + shift) % 26;
            }
            crypto_char += c;
        }
        cout << crypto_char << endl;
    }

    return 0;
}
