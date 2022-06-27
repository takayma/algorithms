def selection_sort(a):
    arr = a.copy()
    for i in range(len(arr) - 1):
        _i = i
        for j in range(i + 1, len(arr)):
            if (arr[j] < arr[_i]):
                _i = j
        arr[_i], arr[i] = arr[i], arr[_i]
    return arr
