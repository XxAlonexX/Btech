#include <iostream>
using namespace std;

struct PolyNode {
    int coeff, exp;
    PolyNode* next;
    PolyNode(int c, int e) : coeff(c), exp(e), next(nullptr) {}
};

void addPolynomial(PolyNode* p1, PolyNode* p2) {
    while (p1 && p2) {
        if (p1->exp > p2->exp) {
            cout << p1->coeff << "x^" << p1->exp << " + ";
            p1 = p1->next;
        } else if (p1->exp < p2->exp) {
            cout << p2->coeff << "x^" << p2->exp << " + ";
            p2 = p2->next;
        } else {
            cout << (p1->coeff + p2->coeff) << "x^" << p1->exp << " + ";
            p1 = p1->next;
            p2 = p2->next;
        }
    }
    while (p1) {
        cout << p1->coeff << "x^" << p1->exp << " + ";
        p1 = p1->next;
    }
    while (p2) {
        cout << p2->coeff << "x^" << p2->exp << " + ";
        p2 = p2->next;
    }
    cout << "0\n";
}

int main() {
    PolyNode* poly1 = new PolyNode(3, 2);
    poly1->next = new PolyNode(5, 1);

    PolyNode* poly2 = new PolyNode(4, 2);
    poly2->next = new PolyNode(6, 0);

    addPolynomial(poly1, poly2);
    return 0;
}
