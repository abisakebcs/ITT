#include <iostream>
using namespace std;

// Function to display the matrix
void displayMatrix(int D[][100], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (D[i][j] == 9999)
                cout << "INF\t";
            else
                cout << D[i][j] << "\t";
        }
        cout << "\n";
    }
}

// Main Floyd's Algorithm Function
void floydAlgorithm(int W[][100], int D[][100], int n) {
    // Step 1: Initialize D with W
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            D[i][j] = W[i][j];
        }
    }

    // Step 2: Floyd's Algorithm
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (D[i][k] != 9999 && D[k][j] != 9999) {
                    if (D[i][k] + D[k][j] < D[i][j]) {
                        D[i][j] = D[i][k] + D[k][j];
                    }
                }
            }
        }
    }
}

// Main Function
int main() {
    int n;

    cout << "Enter number of vertices: ";
    cin >> n;

    int W[100][100];

    cout << "\nEnter weight matrix values (9999 for INF):\n";
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << "W[" << i << "][" << j << "]: ";
            cin >> W[i][j];
        }
    }

    int D[100][100];

    cout << "\n=== FLOYD'S ALGORITHM ===\n\n";
    cout << "Original Matrix:\n";
    displayMatrix(W, n);

    floydAlgorithm(W, D, n);

    cout << "\nShortest Path Matrix:\n";
    displayMatrix(D, n);

    return 0;
}