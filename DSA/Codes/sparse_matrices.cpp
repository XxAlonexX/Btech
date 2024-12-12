#include <iostream>
#include <vector>
using namespace std;

void sparseMatrix(vector<vector<int>> matrix) {
    for (int i = 0; i < matrix.size(); i++)
        for (int j = 0; j < matrix[i].size(); j++)
            if (matrix[i][j] != 0)
                cout << "(" << i << ", " << j << ", " << matrix[i][j] << ")\n";
}

int main() {
    vector<vector<int>> matrix = {{5, 0, 0}, {0, 8, 0}, {0, 0, 3}};
    sparseMatrix(matrix);
    return 0;
}
