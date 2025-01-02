#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    float x, media;
    int count = 0;
    int r = 1;
    while(r != 2) {
        cin >> x;
        if (x <= 10 && x >= 0) {
            media += x;
            count++;
        } else {
            cout << "nota invalida\n";
        }
        if (count == 2) {
            cout << "media = " << fixed << setprecision(2) << media/count << endl;
            count = 0;
            media = 0;
            do {
                cout << "novo calculo (1-sim 2-nao)\n";
                cin >> r;
            } while (r != 2 && r != 1);
        }
    }
    return 0;
}