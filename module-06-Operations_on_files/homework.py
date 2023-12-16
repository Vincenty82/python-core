### IMPORT


### ZADANIA

# ZAD.1

example_path_1 = r".\hw_sup_files\zad1.txt"

def total_salary(path):
    opened_file = open(path, "r")
    try:
        salaries_sum = 0.0
        while True:
            line = opened_file.readline()
            if not line:
                break
            _, salary = line.split(",")
            salaries_sum += float(salary)
    finally:
        opened_file.close()
    return salaries_sum

# ZAD.2

example_path_2 = r".\hw_sup_files\zad2.txt"
example_employee_list = [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]

def write_employees_to_file(employee_list, path):
    opened_file = open(path, "w")
    try:
        for dep_list in employee_list:
            for employee in dep_list:
                opened_file.write(employee + "\n")
    finally:
        opened_file.close()
    return

# ZAD.3

def read_employees_from_file(path):
    opened_file = open(path, "r")
    try:
        line_list = []
        for line in opened_file.readlines():
            line_list.append(line.removesuffix("\n"))
    finally:
        opened_file.close()
    return line_list

# ZAD.4

example_record = "Drake Mikelsson,19"

def add_employee_to_file(record, path):
    opened_file = open(path, "a")
    try:
        opened_file.write(record + "\n")
    finally:
        opened_file.close()
    return

# ZAD.5
# ZAD.6
# ZAD.7
# ZAD.8
# ZAD.9
# ZAD.10
# ZAD.11
# ZAD.12
# ZAD.13
# ZAD.14

### WYWOLANIA

if __name__ == "__main__":

    # LISTA FUNKCJI DO WYKONANIA
    
    functions_to_execute = [
        # total_salary(example_path_1),
        # write_employees_to_file(example_employee_list, example_path_2),
        # read_employees_from_file(example_path_2),
        add_employee_to_file(example_record, example_path_2),
    ]
    
    # WYKONANIE FUNKCJI I WYŚWIETLENIE WYNIKÓW
    
    if functions_to_execute:
        print()
        for single_function in functions_to_execute:
            print(f"return = {single_function}")
        print()
    else:
        print("\nWybierz funkcję z listy funkcji do wykonania.\n")