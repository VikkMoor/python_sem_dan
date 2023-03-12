"""Function sum(a, b) that returns the sum of two non-negative numbers.
Can use only +1 and -1 arithmetic operations. Without any loops."""


def my_sum(a, b):
    if b == 0:
        return a
    return a + my_sum(1, b - 1)


A = int(input("Enter A: "))
B = int(input("Enter B: "))
print(my_sum(A, B))
