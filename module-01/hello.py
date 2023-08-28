print("""
Hello World!
This is my first lesson.
""")

# Asking about age with lack of input check

def input_check(age):
    if len(age) == 0:
        return False
    else:
        age = int(age)
        return True

ADULT_THR = 18
user_status = "udefined"
age = input("Can you please type your age? ")
input_result=input_check(age)
    
#if (input_result == True) and (age >= ADULT_THR):
#    user_status = "an adult"
#    print(f"You are {user_status}.")
#elif (input_result == True) and (age < ADULT_THR):
#    user_status = "a child"
#    print(f"You are {user_status}.")
#else:
#    print("You didn't give your age.")

print(f"\ninput_check = {input_check(age)}\nuser_status = {user_status}\nage variable type = {type(age)}") # print variables



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