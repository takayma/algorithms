#include <iostream>
#include <vector>

using namespace std;

vector<int> merge_sort(vector<int> a) {
    vector<vector<int>> arr;
    for (int i = 0; i < a.size() - 1; i += 2) {
        if (a[i + 1] > a[i]) {
            arr.push_back(vector<int> {a[i], a[i + 1]});
        } else {
            arr.push_back(vector<int> {a[i + 1], a[i]});
        }
    }
    if (a.size() % 2 == 1) arr.push_back(vector<int> {a[a.size() - 1]});

    int i = 0;
    vector<vector<int>> _arr;
    while (arr.size() != 1) {
        _arr.push_back({});
        int il = _arr.size() - 1;

        int ia = 0, ib = 0;
        int la = arr[i].size(), lb = arr[i + 1].size();
        while (ia < la and ib < lb) {
            if (arr[i][ia] < arr[i + 1][ib]) {
                _arr[il].push_back(arr[i][ia]);
                ++ia;
            } else {
                _arr[il].push_back(arr[i + 1][ib]);
                ++ib;
            }
        }
        if (ia < la) {
            for (int j = ia; j < la; ++j) _arr[il].push_back(arr[i][j]);
        }
        if (ib < lb) {
            for (int j = ib; j < lb; ++j) _arr[il].push_back(arr[i + 1][j]);
        }

        i += 2;

        if (i >= arr.size() - 1) {
            if (arr.size() % 2 == 1) {
                _arr.push_back(arr[arr.size() - 1]);
            }
            i = 0;
            arr = _arr;
            _arr.clear();
        }
    }

    return arr[0];
}

int main() {
    vector<int> arr {1, -1, 3, 9, 0, 0, 4, 2, -5};
    arr = merge_sort(arr);
    for (auto x : arr) cout << x << ' ';
}
