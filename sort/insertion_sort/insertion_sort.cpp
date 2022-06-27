#include <iostream>
#include <vector>

using namespace std;

vector<int> insertion_sort (vector<int> arr) {
    for (int i = 1; i < arr.size(); ++i) {
        int j = i;
        while (arr[j - 1] >= arr[i] and j > 0) --j;
        arr.insert(arr.begin() + j, arr[i]);
        arr.erase(arr.begin() + i + 1);
    }
    
    return arr;
}

int main() {
    vector<int> arr {1, -1, 3, 9, 0, 0, 4, 2, -5};
    arr = insertion_sort(arr);
    for (auto x : arr) cout << x << ' ';
}
