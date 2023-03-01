"""Task bout "scrabble" game and counting the price of english/russian word"""
points = {1: 'АВЕИНОРСТAEIOULNSTR',
          2: 'ДКЛМПУDG',
          3: 'БГЁЬЯBCMP',
          4: 'ЙЫFHVWY',
          5: 'ЖЗХЦЧK',
          8: 'ШЭЮJZ',
          10: 'ФЩЪQZ'}
word = input('Enter your word: ').upper()
price = 0
for i in word:
    if i in ''.join(points.values()):
        for j in points:
            if i in points[j]:
                price += j
print(price)
