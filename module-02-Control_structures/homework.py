# x=43

# if x % 2:
#     print("odd")
# else:
#     print("even")

# y=0
# msg = "0123456789"
# for x in msg:
#     print(x)
#     y += 1
# print(y)

# x = int(input("\nPodaj liczbę dziesiętną: "))
# result = ""
# while x != 0:
#     bit = str(x % 2)
#     print(f"bit: {bit}")
#     x = x // 2
#     print(f"x: {x}")
#     result = bit + result
# print(f"Liczba binarna: {result}\n")

# ZADANIE 7

# num = int(input("Enter the integer (0 to 100): "))
# sum = 0
# n = 0
# while n <= num:
#     sum = sum + n
#     n += 1
# print(sum)

# ZADANIE 8

# message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
# search = "r"
# result = 0
# for char in message:
#     if char == search:
#         result += 1
#         print(result)

# ZADANIE 9

# first = int(input("Enter the first integer: "))
# second = int(input("Enter the second integer: "))
# gcd = first if first < second else second
# print(f"{gcd} jest mniejsza.")
# while first % gcd != 0:
#     gcd = gcd - 1
# #    print(gcd)
#     while second % gcd != 0:
#         gcd = gcd -1
# #        print(gcd)
# print(gcd)

# ZADANIE 10

# num = int(input("Enter integer (0 for output): "))
# sum = 0
# while num:
#     for i in range(num + 1):
#         sum = sum + i
#         print(f"i={i} sum={sum}")  # Print each step
#     num = int(input("Enter integer (0 for output): "))
# print(f"Final sum:{sum}")

# ZADANIE 11

# sum = 0
# while True:
#     num = int(input("Enter integer (0 for output): "))
#     if num == 0:
#         break
#     for i in range(num + 1):
#         sum = sum + i
#         print(f"i={i} sum={sum}")
# print(f"Final sum:{sum}")

# ZADANIE 12

# sum = 0
# while True:
#     num = int(input("Enter integer (0 for output): "))
#     if num == 0:
#         break
#     for i in range(num + 1):
#         if i % 2:
#             continue
#         sum = sum + i
#         print(f"i={i} sum={sum}")
# print(f"Final sum:{sum}")

# ZADANIE 13 <-- SZYFR CEZARA

message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
for ch in message:
    if "A" <= ch <= "Z":
        pos = ord(ch) - ord("A")
        pos = (pos + offset) % 26
        new_char = chr(pos + ord("A"))
        encoded_message += new_char
    elif "a" <= ch <= "z":
        encoded_message += chr((((ord(ch) - ord("a")) + offset) % 26) + ord("a"))
    else:
        encoded_message += ch
print(encoded_message)

# ZADANIE 14

# pool = 1000
# quantity = int(input("Enter the number of mailings: "))
# try:
#     chunk = pool // quantity
# except ZeroDivisionError:
#     print('Divide by zero completed!')

# ZADANIE 15

# result = 0.0
# operand = 0.0
# operator = "+"
# wait_for_number = True

# while True:
#     if wait_for_number:
#         try:
#             operand = input(">>> ")
#             if operator == "+":
#                 result = result + float(operand)
#             elif operator == "-":
#                 result = result - float(operand)
#             elif operator == "/":
#                 result = result / float(operand)
#             else:
#                 result = result * float(operand)
#             wait_for_number = False
#             continue
#         except ValueError:
#             print(f"\'{operand}\' nie jest liczbą. Spróbuj ponownie")
#     else:
#         operator = input(">>> ")
#         while operator not in ["+","-","/","*","="]:
#             print(f"{operator} nie jest \'+\' lub \'-\' lub \'/\' \'*\'. Spróbuj ponownie")
#             operator = input(">>> ")
#         if operator in ["+","-","/","*"]:
#             wait_for_number = True
#             continue
#         elif operator == "=":
#             print(f"Wynik: {result}")
#             break
