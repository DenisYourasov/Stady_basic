from random import randint

n = int(input('Enter the length of the list: '))
l = [randint(-99, 99) for i in range(n)]

print('Initial list:', l)

for i in range(len(l)):
	min_value_index = i
	for j in range(i + 1, len(l)):
		if l[j] < l[min_value_index]:
			min_value_index = j
	l[i], l[min_value_index] = l[min_value_index], l[i]

print('Sorted list:', l)