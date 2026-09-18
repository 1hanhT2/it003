// calculate the value of a function
// ax^2 + bx + c
//

#include <cmath>
#include <iostream>

using namespace std;

int main() {

    // for (int i = 0; i < 3; i++) {
    //     cout << "Nhap cac gia tri can nhap cua" << '\n';

    // }

    cout << "Nhap cac gia tri cua A, B, C cua phuong trinh " << '\n';
    double first, second, third;
    cin >> first >> second >> third;
    cout << "Nhap gia tri x" << '\n';
    double x;
    cin >> x;
    auto value = first * pow(x, 2) + second * x + third;
    cout << "Gia tri cua phuong trinh la: " << value << '\n';

    return 0;
}
