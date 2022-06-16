a = [1, -1, 3, 9, 0, 0, 4, 2, -5]
a.sort()
x = 9

def binary_search(arr, key):
	l = int(len(arr) / 2)
	i = l
	while arr[i] != key:
		l = int(l / 2)
		if key < arr[i]:
			i -= max(l, 1)
		else:
			i += max(l, 1)

	return i

i = binary_search(a, x)
print(i, a[i], x)