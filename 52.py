#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int tt;
    cin >> tt;
    while (tt--) {
        string str;
        cin >> str;

        // count total 'u' in the string
        long long aftU = 0;
        for (char c : str)
            if (c == 'u')
                aftU++;

        long long befU = 0;
        long long ans  = 0;
        for (char c : str) {
            if (c == 'u') {
                // move this 'u' from after to before
                aftU--;
                befU++;
            }
            else if (c == 'w') {
                // each 'w' pairs with any 'u' before and any 'u' after
                ans += befU * aftU;
            }
        }

        cout << ans << "\n";
    }
    return 0;
}
