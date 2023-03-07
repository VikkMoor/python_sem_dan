"""Function sum(a, b) that returns the sum of two non-negative numbers.
Can use only +1 and -1 arithmetic operations. Without any loops."""


def my_sum(a, b):
    a += 1
    b -= 1
    if b > 0:
        return my_sum(a, b)
    else:
        return a


A = int(input("Enter A: "))
B = int(input("Enter B: "))
print(my_sum(A, B))
