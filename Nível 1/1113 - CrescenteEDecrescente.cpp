#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int x, y;
    while (true) {
        cin >> x >> y;
        if (x > y) {
            cout << "Decrescente\n";
        } else if (y > x) {
            cout << "Crescente\n";
        } else {
            break;
        }
    }
}