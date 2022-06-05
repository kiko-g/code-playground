#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
using namespace std;
vector<int> minimums;

void printAllPath(vector<vector<int>> matrix, vector<vector<int>> hash, int n, int m, int i, int j, vector<int> result = {}) {
    if (i < 0 || j < 0 || i >= n || j >= m || hash[i][j] == 1) return;
    if (i == n - 1 && j == m - 1) {
        vector<int> v;
        result.push_back(matrix[i][j]); // push the last element
        int minimum = 1000000001;
        for (int k : result) if (k < minimum) minimum = k;
        minimums.push_back(minimum);

        return;
    }

    hash[i][j] = 1;
    result.push_back(matrix[i][j]);               // store the path
    printAllPath(matrix, hash, n, m, i, j + 1, result); // go to the right
    printAllPath(matrix, hash, n, m, i + 1, j, result); // go to the down
    printAllPath(matrix, hash, n, m, i - 1, j, result); // go to the up
    printAllPath(matrix, hash, n, m, i, j - 1, result); // go to the left
    result.pop_back();                         // pop the last element
    hash[i][j] = 0;                         // hash position 0 for traverse another path
}


vector<int> readVector() {
    string line, word;
    getline(cin, line);
    istringstream input(line);
    vector<int> output;
    while (input >> word) {
        int i = std::stoi(word);
        output.push_back(i);
    }

    return output;
}



int main() {
    int n, m;
    cin >> n >> m;
    cin.ignore();

    vector<vector<int>> matrix;
    for (int i = 0; i < n; i++) {
        vector<int> aux = readVector();
        matrix.push_back(aux);
    }

    vector<vector<int>> hash(n, vector<int>(m, 0));
    printAllPath(matrix, hash, n, m, 0, 0);

    int max_min = -1;
    for (int it : minimums)
        if(it > max_min) max_min = it;
    cout << max_min;

    return 0;
}
