#include <cmath>
#include <iostream>

using namespace std;

int main() {
    double a, b, c;
    cin >> a >> b >> c;
    double avgS = (a + b + c) / 3;
    double avgM = cbrt(a * b * c);

    cout << "Gia tri trung binh cong la " << avgS << '\n';
    cout << "Gia tri trung binh nhan la " << avgM << '\n';

    return 0;
}
