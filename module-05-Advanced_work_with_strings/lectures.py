# s = "This is a string"
# s = s.removeprefix("dupa")
# print(len(s))
# s = s.center(18, "-")
# print(s)

# value = 100
# print(f"value = {value:b}")

# with open("hello.txt", "r") as file:
#     file.seek(2, 2)
#     ch = file.read(1)
#     print(ch)

# for i in range(16):
#     s = "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(i)
#     print(s)

# width = 5
# for num in range(12):
#     print('{:^10} {:^10} {:^10}'.format(num, num**2, num**3))

# print("{name} {last_name}".format(last_name="Dilan", name="Bob"))           # Bob Dilan
# print("{name!r} {last_name!s}".format(last_name="Dilan", name="Bob"))       # 'Bob' Dilan

# print('dec: {:d} hex: {:x} bin: {:b}'.format(15, 15, 15))                   # dec: 15 hex: f bin: 1111
# print(f'dec: {15:d} hex: {15:x} bin: {15:b}')                               # dec: 15 hex: f bin: 1111

# print('pi: {:0.3}'.format(3.1415))                                          # pi: 3.14
# print(f'pi: {3.1415:0.3}')                                                  # pi: 3.14

# print('"{}" "{:+}" "{:-}" "{: }"'.format(1, 2, -3, 4))                      # "1" "+2" "-3" " 4"
# print(f'"{1}" "{2:+}" "{-3:-}" "{4: }"')                                    # "1" "+2" "-3" " 4"

# print("|{:<10}|{:*^10}|{:>10}|".format('left', 'center', 'right'))          # |left      |**center**|     right|
# print(f"|{'left':<10}|{'center':*^10}|{'right':>10}|")                      # |left      |**center**|     right|

import re

s1 = "I am 25 years old"
age = re.search('\d+', s1)
print(age)                                                                    # <re.Match object; span=(5, 7), match='25'>

age2 = re.search('\d+', s1)
print(age2.group())                                                           # 25

s2 = "I bought 7 nuts for 6$ and 10 bolts for 3$."
numbers = re.findall('\d+', s2)
print(numbers)                                                                # ['7', '6', '10', '3']

p = re.sub(r'(blue|white|red)', 'colour', 'blue socks and red shoes')
print(p)                                                                      # colour socks and colour shoes
