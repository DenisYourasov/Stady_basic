# Программа предназначена для выравнивания текста (из внешнего файла) по ширине аналогично функции в MSWord.

while True:
	len_str = input('Please enter a string length between 35 and 80 characters: ')

	if not len_str.isdigit():
		print('\nPlease enter an integer value.\n')
		continue

	len_str = int(len_str)

	if len_str < 35 or len_str > 80:
		print('\nPlease enter a length within the given range.\n')
		continue

	break

len_str = int(len_str) + 1

# - очистка нового файла.
f =  open('textformat.txt', 'w') 
f.close()

with open('text.txt', 'r') as origin, open('textformat.txt', 'a') as formated:

	cursor_location = 0

	while True:
		row = origin.read(len_str)

		if not row:
			break

		if '\n' in row:
			new_line_index = row.find('\n')
			row = row[:new_line_index].strip()
		elif row[-1] == ' ':
			row = row.strip()
		elif row[-1] != ' ':
			space_index = row.rfind(' ')
			row = row[:space_index].strip()
		elif row[-2] == ' ':
			row = row[:-2].strip()

		cursor_location += len(row)  + 1
		origin.seek(cursor_location)

		amount_space = row.count(' ')
		amount_space_add = (len_str - 1) - len(row)

		while len(row) < (len_str - 1):
			if len(row) == 0:
				break
			elif ' ' not in row:
				break
			elif len(row) == (len_str - 1):
				break
			elif row[-1] == '.':
				break
			elif amount_space_add <= amount_space:
				row = row.replace(' ', '  ', amount_space_add)
			elif amount_space_add > amount_space:
				row = row.replace(' ', '  ', amount_space_add)
				amount_space_add -= amount_space

		formated.write(row + '\n')

print('Your wish is granted and create new file "textformat.txt"!')