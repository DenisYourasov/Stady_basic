from random import randint

n = int(input('Enter the length of the list: '))
l = [randint(-99, 99) for i in range(n)]

counter = 0

print('Initial list: ', l)

for i in range(len(l) - 1):
	for j in range(len(l) - i - 1):
		if l[i] > l[i + 1]:
			l[i], l[i + 1] = l[i + 1], l[i]
			counter += 1
		if counter == 0:
			break

print('Sorted list: ', l)