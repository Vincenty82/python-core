# ZADANIE 1

# def amount_payment(payment):
#     sum = 0
#     for amount in payment:
#         if amount > 0:
#             sum = sum + amount
#     return sum

# ZADANIE 2

# def prepare_data(data):
#     sorted_data = sorted(data)
#     sorted_data.pop(0)
#     sorted_data.pop(-1)
#     return sorted_data

# ZADANIE 3

# def format_ingredients(items):
#     if len(items) <= 1:
#         try:
#             return items[0]
#         except IndexError:
#             return ""
#     else:
#         formatted_ingredients = items[0]    
#         for item in items[1:len(items)-1]:
#             formatted_ingredients = formatted_ingredients + ", " + item
#         formatted_ingredients = formatted_ingredients + " and " + items[-1] 
#     return formatted_ingredients

# ZADANIE 4

# def get_grade(key):
#     ECTS = {"F":1,"FX":2,"E":3,"D":3,"C":4,"B":5,"A":5}
#     return ECTS.get(key)
# def get_description(key):
#     ECTS = {"F":"Unsatisfactorily","FX":"Unsatisfactorily","E":"Enough","D":"Satisfactorily","C":"Good","B":"Very good","A":"Perfectly"}
#     return ECTS.get(key)

# ZADANIE 5

# def lookup_key(data, value):
#     result = []
#     for key, val in data.items():
#         if val == value:
#             result.append(key)
#     return result

# ZADANIE 6

# def split_list(grades):
#     less_than_average = []
#     more_than_average = []
#     average = 0
#     if grades != []:
#         for grade in grades:
#             average = average + grade
#         average = average / len(grades)
#         for grade in grades:
#             if grade <= average:
#                 less_than_average.append(grade)
#                 less_than_average.sort()
#             else:
#                 more_than_average.append(grade)
#                 more_than_average.sort()
#     return (less_than_average, more_than_average)

# ZADANIE 7

# points = {
#     (0, 1): 2,
#     (0, 2): 3.8,
#     (0, 3): 2.7,
#     (1, 2): 2.5,
#     (1, 3): 4.1,
#     (2, 3): 3.9,
# }

# def calculate_distance(coordinates):
#     distance = 0
#     if len(coordinates) > 1:
#         for i in range(len(coordinates) - 1):
#             point = [coordinates[i], coordinates[i+1]]
#             point.sort()
#             point = tuple(point)
#             if point in points:
#                 distance = distance + points[point]
#         return distance
#     return distance

# ZADANIE 8