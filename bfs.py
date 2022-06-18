l = [[],		#Это для нуля, которого нет
	[2, 3, 4],	#1
	[1],		#2
	[1, 7, 8],	#3
	[1, 5, 6],	#4
	[4],		#5
	[4, 8],		#6
	[3, 8],		#7
	[3, 6, 7]]	#8

def bfs(l, start):
	a = [start]
	b = {start : 0}
	i = 0
	while i < len(a):
		for x in l[a[i]]:
			if x not in a:
				a.append(x)
				b[x] = b[a[i]] + 1

		i += 1

	return b

c = bfs(l, 1)
for i in sorted(c):
	print(f'{i}: {c[i]}')