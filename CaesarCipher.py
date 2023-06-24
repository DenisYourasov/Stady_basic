# Запрашиваем у пользователя режим работы программы и вводные данные:
# шифрование или дешифровка, язык, шаг, текст; и проверяем ввод на корректность значений.

whats_direction = input('Program operation mode: encryption (E) or decryption (D)? \n').lower()
while whats_direction != 'e' and whats_direction != 'd':
	whats_direction = input('Invalid entry, enter E or D. \n').lower()

whats_language = input('Choose language: Russian (R) or English (E)? \n').lower()
while whats_language != 'r' and whats_language != 'e':
	whats_language = input('Invalid entry, enter R or E. \n').lower()

whats_step = input('Choose cipher step. \n')
while whats_step.isdigit() != True:
	whats_step = input('Invalid input, write an integer. \n')

whats_text = input('Enter you text: \n')
while whats_text.isspace() == True:
	whats_text = input('Invalid input, enter text. \n')

# Объявляем функцию с четырьмя введенными аргументами.
def caesar(direction, language, step, text):

	# Задаем 4 словаря строками с двумя алфавитами.
	upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
	upper_rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
	lower_rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

	# Объявляем цикл - количество итераций равно длине строки text.
	for i in range(len(text)):
		# Задаем локальные переменные: длину алфавита и значения словарей.
		if language == 'r':
			alphas = 32
			low_alphabet = lower_rus_alphabet
			upp_alphabet = upper_rus_alphabet
		if language == 'e':
			alphas = 26
			low_alphabet = lower_eng_alphabet
			upp_alphabet = upper_eng_alphabet
		# Если элемент в исходном тексте является буквой:
		if text[i].isalpha():
			# Находим место символа [i] в словаре upp_alphabet либо low_alphabet.
			if text[i] == text[i].lower():
				place = low_alphabet.index(text[i])
			if text[i] == text[i].upper():
				place = upp_alphabet.index(text[i])
			# При дешифровке:
			if direction == 'd':
				# новый индекс = старый индекс - шаг % длина алфавита
				index = (place - int(step)) % alphas
			# При шифровании:
			elif direction == 'e':
				# новый индекс = старый индекс + шаг % длина алфавита
				index = (place + int(step)) % alphas
			# Выводим измененный символ.
			if text[i] == text[i].lower():
				print(low_alphabet[index], end='')
			if text[i] == text[i].upper():
				print(upp_alphabet[index], end='')
		# Если элемент в исходном тексте не является буквой: выводим символ без изменений
		else:
			print(text[i], end='')

caesar(whats_direction, whats_language, whats_step, whats_text)