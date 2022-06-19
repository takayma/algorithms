#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int binary_search (vector<int> arr, int key) {
    int l = arr.size() / 2;
    int i = l;
    while (arr[i] != key) {
        l /= 2;
        if (arr[i] > key) {
            i -= max(l, 1);
        } else {
            i += max(l, 1);
        }
    }
    return i;
}

int main () {
    vector<int> arr{1, -1, 3, 9, 0, 0, 4, 2, -5};
    sort(arr.begin(), arr.end());
    for (auto x : arr) cout << x << ' ';
    cout << endl;
    int x = 9;
    int i = binary_search(arr, x);
    cout << i << endl;
}