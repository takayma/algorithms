def insertion_sort(a):
    arr = a.copy()
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] >= arr[i] and j > 0:
            j -= 1
        arr.insert(j, arr.pop(i))

    return arr
