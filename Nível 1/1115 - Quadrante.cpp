#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int x, y;
    while (true) {
        cin >> x >> y;
        if (x == 0 || y == 0)
            break;
        if (x > 0) {
            if (y > 0) {
                cout << "primeiro\n";
            } else {
                cout << "quarto\n";
            }
        } else {
            if (y > 0) {
                cout << "segundo\n";
            } else {
                cout << "terceiro\n";
            }
        }
    }
    return 0;
}