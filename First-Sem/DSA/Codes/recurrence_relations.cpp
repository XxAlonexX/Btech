#include <iostream>
using namespace std;

// Recursive function for T(n)
int solveRecurrence(int n) {
    if (n == 1) return 1; // Base case
    return 2 * solveRecurrence(n / 2) + n;
}

// Test
int main() {
    int n = 8; // Example input size
    cout << "T(" << n << ") = " << solveRecurrence(n) << endl;
    return 0;
}
