def merge_sort(a):
    arr = []
    for i in range(0, len(a) - 1, 2):
        if a[i + 1] > a[i]:
            arr.append([a[i], a[i + 1]])
        else:
            arr.append([a[i + 1], a[i]])
    if len(a) % 2 == 1:
        arr.append([a[-1]])

    i = 0
    _arr = []
    while len(arr) != 1:
        _arr.append([])
        ia, ib = 0, 0
        la, lb = len(arr[i]), len(arr[i + 1])
        while ia < la and ib < lb:
            if arr[i][ia] < arr[i + 1][ib]:
                _arr[-1].append(arr[i][ia])
                ia += 1
            else:
                _arr[-1].append(arr[i + 1][ib])
                ib += 1
        if ia < la:
            _arr[-1] += arr[i][ia:]
        if ib < lb:
            _arr[-1] += arr[i + 1][ib:]

        i += 2

        if i >= len(arr) - 1:
            if len(arr) % 2 == 1:
                _arr.append(arr[-1])
            i = 0
            arr = [*_arr]
            _arr = []

    return arr[0]
