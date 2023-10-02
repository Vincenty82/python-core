# for i in range(200):
#     print(f"{i} = {chr(i)}")
#     #  print(chr(i), end=", ")
#     i += 1

# def say_hello(name=None):
#     if name is None:
#         print(f"Hello stranger")
#     else:
#         print(f"Hello {name}")

# say_hello("Bob")
# say_hello()

# def add(a, b):
#     return a + b
# c = lambda a, b: a + b
# print(c(2, 3))

from functools import lru_cache

counter=0

# def fib(n):  #iteracyjny
#     global counter
#     counter += 1
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#     return a

@lru_cache  #dekorator redukcja rekurencji
def fib(n):  # rekurencyjny
    global counter
    counter += 1
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

def print_fib(n):
    for _ in range(n+1):
        print(f"Element: {_}   Wartość: {fib(_)}")

print_fib(int(input()))
print(f"Countrer: {counter}")

# W Konspekcie mowa jest o Punkcie Wejścia. Jest czas by to omówić?