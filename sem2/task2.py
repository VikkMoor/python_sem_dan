"""Task bout finding the element in list with close-in value to number X"""

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
X = int(input('Enter the number X: '))
new_list = []
for i in range(N):
    new_list.append(abs(X - my_list[i]))
x = new_list.index(min(new_list))
print(my_list[x])
