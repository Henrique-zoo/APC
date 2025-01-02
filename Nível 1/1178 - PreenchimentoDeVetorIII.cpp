#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    double n;
    cin >> n;
    for (int i = 0; i < 100; i++)
        cout << fixed << setprecision(4) << "N[" << i << "] = " << n / pow(2, i) << endl;

    return 0;
}