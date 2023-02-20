"""Sum of digits in three-digit number"""

a = int(input('Enter a 3-digit number: '))
if a < 100 or a > 999:
    print('Please, enter correct number.')
else:
    print(f'The sum of digits is: {a % 10 + a // 10 % 10 + a // 100}')
