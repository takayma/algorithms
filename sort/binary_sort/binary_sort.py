def binary_sort(a):
    length = len(a)
    if length <= 1:
        return a
    mid = int(length / 2)
    mid = a.pop(mid)
    left, right = [], []
    for x in a:
        if x <= mid:
            left.append(x)
        else:
            right.append(x)
    return binary_sort(left) + [mid] + binary_sort(right)
