// number categorization: +- =0 mod2
//
//

#include <cmath>
#include <iostream>

using namespace std;

int main() {
    double a;
    cin >> a;

    if (a == 0) {
        cout << "So A la 0" << '\n';
        return 0;
    }

    if (a > 0) {
        cout << "So A la so duong" << '\n';
    } else {
        cout << "So A la so am" << '\n';
    }

    if (fmod(a, 2.0) == 0) {
        cout << "So a la so chan" << '\n';
    } else {
        cout << "So a la so le" << '\n';
    }

    return 0;
}
