### IMPORT

import base64
import shutil

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

example_path_3 = r".\hw_sup_files\zad5.txt"

def get_cats_info(path):
    with open(path, "r") as opened_file:
        lines_list = []
        for line in opened_file.readlines():
            id_line, name_line, age_line = line.removesuffix("\n").split(",")
            line_dict = {"id":id_line, "name":name_line, "age": age_line}
            lines_list.append(line_dict)
    return lines_list

# ZAD.6

example_path_4 = r".\hw_sup_files\zad6.csv"
example_search_1 = "60b90c1c13067a15887e1ae1"
example_search_2 = "60b90c2413067a15887e1ae2"
example_search_3 = "60b90c2e13067a15887e1ae3"
example_search_4 = "60b90c3b13067a15887e1ae4"
example_search_5 = "60b90c4613067a15887e1ae5"
example_search_6 = "60b90c4613067a15887e1ae6"

def get_recipe(path, search_id):
    with open(path, "r") as opened_file:
        for recepie in opened_file.readlines():
            recepie_list = recepie.removesuffix("\n").split(",")
            if recepie_list[0] == search_id:
                return {"id": recepie_list[0],"name": recepie_list[1], "ingredients": recepie_list[2:]}
    return

# ZAD.7

example_source = r".\hw_sup_files\zad7_source.txt"
example_output = r".\hw_sup_files\zad7_output.txt"

def sanitize_file(source, output):
    with open(source, "r") as source_opened_file:
        with open(output, "w") as target_opened_file:
            target_opened_file.write("".join(character for character in source_opened_file.read() if not character.isdigit()))
    return

# ZAD.8

example_student_list = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]
example_path_5 = r".\hw_sup_files\zad8.csv"

def save_applicant_data(source, output):
    with open(output, "w") as opened_file:
        for student in source:
            student_csv_line = ""
            for value in student.values():
                student_csv_line += str(value) + ","
            opened_file.write(student_csv_line[:-1] + "\n")
    return

# ZAD.9

example_utf8_string_1 = "Hello".encode("utf-8")
example_utf8_string_2 = "World".encode("utf-8")
example_utf16_string_1 = "Hello".encode("utf-16")
example_utf16_string_2 = "World".encode("utf-16")

def is_equal_string(utf8_string, utf16_string):
    if utf8_string.decode("utf-8") == utf16_string.decode("utf-16"):
        return True
    return False

# ZAD.10

example_path_6 = r".\hw_sup_files\zad10.bin"
example_user_credentials_dict = {'andry':'uyro18890D', 'steve':'oppjM13LL9e'}

def save_credentials_users(path, users_info):
    with open(path, "wb") as opened_binary_file:
        for username, password in users_info.items():
            opened_binary_file.write((":".join([username, password]) + "\n").encode())
    return

# ZAD.11

def get_credentials_users(path):
    with open(path, "rb") as opened_binary_file:
        user_list = []
        for line in opened_binary_file.readlines():
            user_list.append(line.decode().removesuffix("\n"))
    return user_list

# ZAD.12

example_user_credentials_list = ['andry:uyro18890D', 'steve:oppjM13LL9e']

def encode_data_to_base64(data):
    base64_encoded_data = []
    for each_user in data:
        base64_encoded_data.append(base64.b64encode(each_user.encode("utf-8")).decode("utf-8"))        
    return base64_encoded_data

# ZAD.13

example_path_7 = "./hw_sup_files"
example_file_name = "zad13.bin"
example_employee_resicence = {
    'Michael': 'Canada',
    'John':'USA',
    'Liza': 'Australia'
    }

def create_backup(path, file_name, employee_residence):
    with open(path + "/" + file_name, "wb") as opened_binary_file:
        for employee_name, country in employee_residence.items():
            opened_binary_file.write((employee_name + " " + country + "\n").encode())
    archive_name = shutil.make_archive("backup_folder", "zip", path)
    return archive_name

# ZAD.14

example_archive_path = "./backup_folder.zip"
example_path_8 = "./hw_sup_files/"

def unpack(archive_path, path_to_unpack):
    shutil.unpack_archive(archive_path,path_to_unpack)
    return

### WYWOLANIA

if __name__ == "__main__":

    # LISTA FUNKCJI DO WYKONANIA
    
    functions_to_execute = [
        # total_salary(example_path_1),
        # write_employees_to_file(example_employee_list, example_path_2),
        # read_employees_from_file(example_path_2),
        # add_employee_to_file(example_record, example_path_2),
        # get_cats_info(example_path_3),
        # get_recipe(example_path_4, example_search_1),
        # sanitize_file(example_source, example_output),
        # save_applicant_data(example_student_list, example_path_5),
        # is_equal_string(example_utf8_string_1,example_utf16_string_1),
        # save_credentials_users(example_path_6,example_user_credentials_dict),
        # get_credentials_users(example_path_6),
        # encode_data_to_base64(example_user_credentials_list),
        # create_backup(example_path_7, example_file_name, example_employee_resicence),
        unpack(example_archive_path,example_path_8),
    ]
    
    # WYKONANIE FUNKCJI I WYŚWIETLENIE WYNIKÓW
    
    if functions_to_execute:
        print()
        for single_function in functions_to_execute:
            print(f"return = {single_function}")
        print()
    else:
        print("\nWybierz funkcję z listy funkcji do wykonania.\n")