# ZADANIE 1

def amount_payment(payment):
    sum = 0
    for amount in payment:
        if amount > 0:
            sum = sum + amount
    print(f"payment = {payment}")
    print(f"sum = {sum}")
    return sum

# ZADANIE 2

def prepare_data(data):
    sorted_data = sorted(data)
    sorted_data.pop(0)
    sorted_data.pop(-1)
    print(f"data = {data}")
    print(f"sorted_data = {sorted_data}")
    return sorted_data

# ZADANIE 3

def format_ingredients(items):
    if len(items) <= 1:
        try:
            return items[0]
        except IndexError:
            return ""
    else:
        formatted_ingredients = items[0]    
        for item in items[1:len(items)-1]:
            formatted_ingredients = formatted_ingredients + ", " + item
        formatted_ingredients = formatted_ingredients + " and " + items[-1] 
    print(f"items = {items}")
    print(f"formatted_ingidients = {formatted_ingredients}")
    return formatted_ingredients

# ZADANIE 4

def get_grade(key):
    ECTS = {"F":1,"FX":2,"E":3,"D":3,"C":4,"B":5,"A":5}
    print(f"key = {key}")
    print(f"ECTS = {ECTS.get(key)}")
    return ECTS.get(key)

def get_description(key):
    ECTS = {"F":"Unsatisfactorily","FX":"Unsatisfactorily","E":"Enough","D":"Satisfactorily","C":"Good","B":"Very good","A":"Perfectly"}
    print(f"key = {key}")
    print(f"Objaśnienie = {ECTS.get(key)}")
    return ECTS.get(key)

# ZADANIE 5

def lookup_key(data, value):
    result = []
    for key, val in data.items():
        if val == value:
            result.append(key)
    print(f"data = {data}")
    print(f"value = {value}")
    print(f"result = {result}")
    return result

# ZADANIE 6

def split_list(grades):
    less_than_average = []
    more_than_average = []
    average = 0
    if grades != []:
        for grade in grades:
            average = average + grade
        average = average / len(grades)
        for grade in grades:
            if grade <= average:
                less_than_average.append(grade)
                less_than_average.sort()
            else:
                more_than_average.append(grade)
                more_than_average.sort()
    print(f"grades = {grades}")
    print(f"less_than_average = {less_than_average}")
    print(f"more_than_average = {more_than_average}")
    return (less_than_average, more_than_average)

# ZADANIE 7

def calculate_distance(coordinates):
    points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
    }
    print(f"coordinates = {coordinates}")
    distance = 0
    if len(coordinates) > 1:
        for i in range(len(coordinates) - 1):
            point = [coordinates[i], coordinates[i+1]]
            point.sort()
            point = tuple(point)
            if point in points:
                distance = distance + points[point]
        print(f"distance = {distance}")
        return distance
    print(f"distance = {distance}")
    return distance

# ZADANIE 8

def game(terra, power):
    print(f"terra = {terra}")
    print(f"power = {power}")
    for level in terra:
        print(f"    level = {level}")
        for enemy_power in level:
            print(f"        enemy_power = {enemy_power}")
            if enemy_power <= power:
                power += enemy_power
                print(f"            win")
                print(f"            power = {power}")
            else:
                print(f"            loss")
                print(f"            power = {power}")
                break
    print(f"return power = {power}")
    return power

# ZADANIE 9

def is_valid_pin_codes(pin_codes):
    print(f"pin_codes = {pin_codes}")
    pin_codes_set = set(pin_codes)
    if pin_codes == []:
        print("List empty.")
        return False
    elif len(pin_codes_set) == len(pin_codes):
        for pin in pin_codes:
            if len(pin) != 4:
                print(f"Invalid list. PIN should have 4 digits. pin = {pin}")
                return False
            else:
                try:
                    int(pin)
                except ValueError: 
                    print(f"Invalid list. PIN cannot have any characters. pin = {pin}")
                    return False
        print("All unique.")
    else:
        print("Invalid list. Not all unique.")
        return False
    return True

# WYWOŁANIA TESTOWE

if __name__ == "__main__":
    # amount_payment([10, 20, -5, 30, 20]) # ZADANIE 1
    # prepare_data([1, -3, 4, 100, 0, -5, 10, 1, 1]) # ZADANIE 2
    # format_ingredients(["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]) # ZADANIE 3
    # get_grade("A") # ZADANIE 4a
    # get_description("A") # ZADANIE 4b
    # lookup_key({'key1': 1, 'key2': 2, 'key3': 3, 'key4': 2}, 2) # ZADANIE 5
    # split_list([1, 12, 3, 24, 5]) # ZADANIE 6
    # calculate_distance([0, 1, 3, 2, 0]) # ZADANIE 7
    # game([[1, 1, 5, 10], [10, 2], [1, 1, 1]], 1) # ZADANIE 6
    is_valid_pin_codes(['1101', '9034', '0011', '12345', '123', '1abc']) # ZADANIE 9
    
    exit
