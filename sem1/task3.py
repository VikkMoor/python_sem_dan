"""lucky bus ticket (6-digit number in Russia) or not"""

tick = int(input('Enter bus ticket number: '))
a = tick // 100000 + (tick // 10000) % 10 + (tick // 1000) % 10
b = (tick // 100 % 10) + (tick // 10 % 10) + tick % 10
if tick < 100000 or tick > 999999:
    print("Enter 6-digit number next time, please.")
elif a == b:
    print('yes')
else:
    print('no')
