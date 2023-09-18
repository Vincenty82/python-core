# ZADANIE 1

# def greeting():
#     print("Hello world!")
# greeting()

# ZADANIE 2

# def invite_to_event(username):
#     return f"Dear {username}, we have the honour to invite you to our event"
# print(invite_to_event("Bartek"))

# ZADANIE 3

# base_rate = 40
# price_per_km = 10
# total_trip = 0

# def calculate_trip_price(distance_km):
#     global total_trip
#     total_trip += 1
#     return base_rate + price_per_km * distance_km

# ZADANIE 4

# def discount_price(price, discount):
#     def apply_discount():
#         nonlocal price
#         price = price - price * discount
#     apply_discount()
#     return price

# ZADANIE 5

# def get_fullname(first_name, last_name, middle_name=""):
#     if middle_name:
#         return first_name + " " + middle_name + " " + last_name
#     else:
#         return first_name + " " + last_name

# ZADANIE 6

# def format_string(string, length, temp_string=""):
#     if len(string) >= length:
#         return string
#     else:
#         for i in range((length - len(string)) // 2):
#             temp_string += " "
#             i += 1
#         return temp_string + string

# ZADANIE 7

# def first(size, *position):  # * Declare tuple
#     return size + len(position)
# def second(size, **comments):  # ** Declare dictionary
#     return size + len(comments)

# ZADANIE 8

# def cost_delivery(quantity, *_, discount=0):  # *_ = Declare unused tuple to ignore everything afrer first argument unless discount is called out by it's name
#     cost = (5 + 2 * (quantity - 1)) * (1 - discount)
#     return cost

# ZADANIE 9

# def cost_delivery(quantity, *_, discount=0):
#     """
#     Funkcja zwraca całkowitą kwotę dostawy.

#     Pierwszym parametrem jest liczba pozycji w zamówieniu. 
#     Parametr rabatu discount, przesyłany tylko za pomocą klucza, domyślnie ma wartość 0.
#     """
#     result = (5 + 2 * (quantity - 1)) * (1 - discount)
#     return result

# ZADANIE 10

# def factorial(n):
#     if n < 2:
#         return 1
#     else:
#         return n * factorial(n - 1)
# def number_of_groups(n, k):
#     return int(factorial(n) / (factorial(n - k) * factorial(k)))

# ZADANIE 11

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)