"""Input - total number of origami (s), output - how much each of 3 kids made (Sergio = Peter, Kate = 2*(Sergio+Peter))"""

s = int(input('Enter total number (multiple of 4): '))
if s % 4 == 0:
    print(f'Peter made: {s // 4)}, Kate made: {s // 2)}, Sergio made: {s // 4}.')
else:
    print("Kids can't made this number of origami cuz of the task.")
