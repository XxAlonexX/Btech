#include <iostream>
using namespace std;

// Binary Search using recursion
int binarySearch(int arr[], int left, int right, int x) {
    if (right >= left) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == x) return mid;
        if (arr[mid] > x) return binarySearch(arr, left, mid - 1, x);
        return binarySearch(arr, mid + 1, right, x);
    }
    return -1;
}

// Fibonacci using recursion
int fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

// Fibonacci using iteration (for comparison)
int fibonacciIterative(int n) {
    if (n <= 1) return n;
    int prev = 0, curr = 1;
    for (int i = 2; i <= n; i++) {
        int temp = curr;
        curr = prev + curr;
        prev = temp;
    }
    return curr;
}

int main() {
    // Binary Search Test
    int arr[] = {2, 3, 4, 10, 40};
    int n = sizeof(arr) / sizeof(arr[0]);
    int x = 10;
    int result = binarySearch(arr, 0, n - 1, x);
    cout << "Binary Search: Element " << x << " found at index " << result << endl;

    // Fibonacci Test
    int fib = 10;
    cout << "Fibonacci(" << fib << ") recursive = " << fibonacci(fib) << endl;
    cout << "Fibonacci(" << fib << ") iterative = " << fibonacciIterative(fib) << endl;
    
    return 0;
}
