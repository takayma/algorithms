def binary_sort(a):
    arr = a.copy()
    length = len(arr)
    if length <= 1:
        return arr
    mid = int(length / 2)
    mid = arr.pop(mid)
    left, right = [], []
    for x in arr:
        if x <= mid:
            left.append(x)
        else:
            right.append(x)
    return binary_sort(left) + [mid] + binary_sort(right)
