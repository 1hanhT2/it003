// find the largest number out of three
//

#include <iostream>

using namespace std;

int main() {
    double a, b, c;
    cin >> a >> b >> c;

    double biggest = a;
    if (b > biggest) {
        biggest = b;
    }
    if (c > biggest) {
        biggest = c;
    }

    cout << "So lon nhat la " << biggest;

    return 0;
}
