# Program for solving a quadratic equation

a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))
D = b**2 - 4 * a * c
print('Discriminant =', D)
if D > 0:
	print('x1 =', (-b + D**0.5) / 2 * a)
	print('x2 =', (-b - D**0.5) / 2 * a)
elif D == 0:
	print('x =', -b / 2 * a)
elif D < 0:
	print('No root')