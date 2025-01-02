#include <bits/stdc++.h>
using namespace std;

int main() {
    for (float i = 0; i < 2.2; i += 0.2) {
        for (float j = 1+i; j < 3.5+i; j++) {
            cout << "I=" << i << " J=" << j << endl;
        }
    }
    return 0;
}