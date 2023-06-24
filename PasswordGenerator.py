# Simple password generator

from random import *

def generate_password(lenght_password, chars):
	password = sample(chars, lenght_password)
	print(''.join(password))

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
exception = 'il1Lo0O'

chars = ''

passwords_number = int(input('Введите количество паролей для генерации: '))
lenght_password = int(input('Введите длину пароля: '))

digit_in_password = input(f'Пароль должен содержать цифры {digits}? - да/нет: ') 
if digit_in_password in ('да', 'ДА', 'Да', 'д', 'y', 'yes', 'Yes', 'YES'):
	chars += digits

uppercase_letters_in_password = input(f'Пароль должен содержать прописные буквы {uppercase_letters}? - да/нет: ')
if uppercase_letters_in_password in ('да', 'ДА', 'Да', 'д', 'y', 'yes', 'Yes', 'YES'):
	chars += uppercase_letters

lowercase_letters_in_password = input(f'Пароль должен содержать строчные буквы {lowercase_letters}? - да/нет: ')
if lowercase_letters_in_password in ('да', 'ДА', 'Да', 'д', 'y', 'yes', 'Yes', 'YES'):
	chars += lowercase_letters

punctuation_in_password = input(f'Пароль должен символы {punctuation}? - да/нет: ')
if punctuation_in_password in ('да', 'ДА', 'Да', 'д', 'y', 'yes', 'Yes', 'YES'):
	chars += punctuation

exception_in_password = input(f'Исключать ли неоднозначные символы {exception}? - да/нет: ')
if exception_in_password in ('да', 'ДА', 'Да', 'д', 'y', 'yes', 'Yes', 'YES'):
	for i in exception:
		chars = chars.replace(i, '')


for i in range(passwords_number):
	generate_password(lenght_password, chars)