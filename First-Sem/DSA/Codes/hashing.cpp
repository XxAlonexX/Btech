#include <iostream>
#include <vector>
using namespace std;

class HashTable {
    vector<int> *table;
    int size;
public:
    HashTable(int size) : size(size) { table = new vector<int>[size]; }
    void insert(int key) { table[key % size].push_back(key); }
    void display() {
        for (int i = 0; i < size; i++) {
            cout << i << ": ";
            for (int key : table[i]) cout << key << " ";
            cout << endl;
        }
    }
};

int main() {
    HashTable ht(5);
    ht.insert(10); ht.insert(15); ht.insert(5); ht.display();
    return 0;
}
