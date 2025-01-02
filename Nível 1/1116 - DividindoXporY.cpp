#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n;
    float x, y;
    cin >> n;
    while (n--) {
        cin >> x >> y;
        if (y != 0) {
            cout << fixed << setprecision(1) << x/y << endl;
        }
        else
            cout << "divisao impossivel\n";
    }
    return 0;
}