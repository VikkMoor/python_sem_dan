"""A^B"""

A = int(input("Enter A: "))
B = int(input("Enter B: "))


def power_a(a, b):
    if b == 0:
        return 1
    return a * power_a(a, b - 1)


print(power_a(A, B))
