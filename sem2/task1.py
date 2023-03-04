"""How many times the number appears in the list"""
from random import randint


def fill_list(n):
    list_1, i = [], 0
    while i < n:
        list_1.append(randint(1, 101))
        i += 1
    return list_1


def print_list(n):
    print(*[i for i in n])


N = int(input('Enter the length of a list: '))
my_list = fill_list(N)
print_list(my_list)
m = int(input('Enter the number to be searched for: '))
count = 0
for i in range(len(my_list)):
    if my_list[i] == m:
        count += 1
print(f'--> {count}')
