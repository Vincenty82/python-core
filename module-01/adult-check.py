print("""
Hello World!
This is my first lesson.
""")
# Asking about age.
def input_check(age): # Empty variable check funcition.
    if len(age) == 0:
        return False
    else:
        return True
ADULT_THR = [18,120]
user_status = None # Reserving the variable
age = input("Type your age: ")
input_check_result = input_check(age)
if input_check_result == True:
    try:
        age = int(age)
    except ValueError:
        print("You did not enter a number. Try using integers.")
        exit()
if input_check_result and ADULT_THR[1] > age >= ADULT_THR[0]:
    user_status = "an adult"
elif (input_check_result == True) and (age < ADULT_THR[0]) and (age < ADULT_THR[1]):
    user_status = "a child"
elif (input_check_result == True) and (age > ADULT_THR[0]) and (age >= ADULT_THR[1]):
    user_status = "immortal?"
else:
    user_status = "without an age?"
print(f"You are {user_status}.\n")
# print(f"\ninput_check_result = {input_check_result}\nuser_status = {user_status}\nage variable type = {type(age)}") # print variables



_do_not_use_this = 0
_not_to_be_trifled_with = "Told you not to use this!"

# print(f"{_not_to_be_trifled_with}")

import math
a = -2
b = 7
c = -6
D = math.pow(b,2) - 4 * a * c
x1 = ( -b - math.pow(D,0.5) ) / ( 2 * a )
x2 = ( -b - math.pow(D,0.5) ) / ( 2 * a )

print(D)
print(x1)
print(x2)