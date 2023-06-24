from decimal import Decimal


def credit_calculator():
	k = Decimal(input('Enter the loan amount: '))
	p = Decimal(input('Enter the interest rate on the loan in %: '))
	n = Decimal(input('Enter loan term, years: '))
	calculatingMethod = input('Choose method of calculating interest on a loan: 1 - Differentiated schedule; 2- Annuity schedule. Please enter 1 or 2: ')
	if calculatingMethod == '1':
		monthlyPayment = k / (n * 12)
		amountRate = 0
		for i in range(int(n) * 12 + 1):
			monthlyRate = (k - monthlyPayment * i) * (p / 100 / 12)
			amountRate += monthlyRate
		print('Total loan payment = ', '{:,.2f}'.format(k + amountRate).replace(',', ' '), end = ', ')
		print('loan repayment amount = ', '{:,.2f}'.format(amountRate).replace(',', ' '))
	else:
		monthlyPayment = k * (p / 100 / 12 + (p / 100 / 12) / ((1 + p / 100 / 12) ** (n * 12) - 1))
		print('Total loan payment = ', '{:,.2f}'.format(monthlyPayment * n * 12).replace(',', ' '), end = ', ')
		print('loan repayment amount = ', '{:,.2f}'.format(monthlyPayment * n * 12 - k).replace(',', ' '))

credit_calculator()
