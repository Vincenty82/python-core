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
if (input_check_result == True) and (age >= ADULT_THR[0]) and (age < ADULT_THR[1]):
    user_status = "an adult"
elif (input_check_result == True) and (age < ADULT_THR[0]) and (age < ADULT_THR[1]):
    user_status = "a child"
elif (input_check_result == True) and (age > ADULT_THR[0]) and (age >= ADULT_THR[1]):
    user_status = "immortal?"
else:
    user_status = "without an age?"
print(f"You are {user_status}.\n")
print(f"\ninput_check_result = {input_check_result}\nuser_status = {user_status}\nage variable type = {type(age)}") # print variables



_do_not_use_this = 0
_not_to_be_trifled_with = "Told you not to use this!"

# print(f"{_not_to_be_trifled_with}")

x = 2
y = x + 10

# print(f"y={y}")

a = 1
b = 2
c = a + b + 10

# print(f"c={c}")