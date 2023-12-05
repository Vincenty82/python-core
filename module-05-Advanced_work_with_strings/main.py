def empty_function():
    return "Wybierz funkcję."

def string_rstrip_method(my_string):
    print("\033[0;46m")
    print(my_string)
    print(my_string.rstrip())
    print("\033[0;0m")
    return "Tadam!"

if __name__ == "__main__":
    functions_to_execute = [
        empty_function(),
        # string_rstrip_method("rstrip -->     ")
    ]
    for f in functions_to_execute:
        print(f)