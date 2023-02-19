"""Input - total number of origami (s), output - how much each of 3 kids made (Sergio = Peter, Kate = 2*(Sergio+Peter))"""

s = int(input('Enter total number (multiple of 4): '))
if s % 4 == 0:
    print(f'Peter made: {int(s / 4)}, Kate made: {int(s / 2)}, Sergio made: {int(s / 4)}.')
else:
    print("Kids can't made this number of origami cuz of the task.")
