# SEKCJA IMPORT

import re

# PUSTA FUNKCJA STARTOWA

def empty_function():
    return

# ZADANIE 1

def real_len(input_string):
    non_escape_char_count = len(input_string)
    escape_sequences = ["\n", "\f", "\r", "\t", "\v"]
    for escape_sequence in escape_sequences:
        non_escape_char_count -= input_string.count(escape_sequence)
    return non_escape_char_count

# ZADANIE 2

articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]

def find_articles(key, letter_case=False):
    matching_articles = []
    for article in articles_dict:
        if letter_case:
            if (key in article.get("title")) or (key in article.get("author")):
                matching_articles.append(article)
        else:
            if (key.casefold() in article.get("title").casefold()) or (key.casefold() in article.get("author").casefold()):
                matching_articles.append(article)
    return matching_articles

# ZADANIE 3

def sanitize_phone_number(phone):
    clean_phone = ""
    for i in phone:
        if i.isdigit():
            clean_phone += i
    return clean_phone

# ZADANIE 4

def is_check_name(fullname, first_name):
    return fullname.startswith(first_name)

# ZADANIE 5

def get_phone_numbers_for_countries(list_phones):
    Japan = []
    Singapore = []
    Taiwan = []
    Ukraine = []
    categorized_phones = {
        "UA": Ukraine,
        "JP": Japan,
        "TW": Taiwan,
        "SG": Singapore
    }
    for phone in list_phones:
        new_phone = sanitize_phone_number(phone)
        if new_phone.startswith("81"):
            Japan.append(new_phone)
        elif new_phone.startswith("65"):
            Singapore.append(new_phone)
        elif new_phone.startswith("886"):
            Taiwan.append(new_phone)
        else:
            Ukraine.append(new_phone)
    return categorized_phones

# ZADANIE 6

def is_spam_words(text, spam_words, space_around=False):
    for word in spam_words:
        if space_around:
            if re.search(r"\b" + word + r"\b", text):
                return True
        else:
            if re.search(word, text):
                return True
    return False

# ZADANIE 7

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}

for cyrillic_char, translation_char in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(cyrillic_char)] = translation_char
    TRANS[ord(cyrillic_char.upper())] = translation_char.upper()

def translate(name):
    return name.translate(TRANS)

# ZADANIE 8

grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}

def formatted_grades(students):
    formatted_students_list = []
    for enumerator, (name, grade) in enumerate(students.items()):
        ects_grade = grades.get(grade)
        formatted_student_grade_pattern = "{:>4}|{:<10}|{:^5}|{:^5}".format(str(enumerator+1), name, grade, str(ects_grade))
        formatted_students_list.append(formatted_student_grade_pattern)
        # print(formatted_student_grade_pattern)                                                        # print rows as they are generated
    return formatted_students_list

# ZADANIE 9

def formatted_numbers():
    formatted_numbers_list = ["|{:^10}|{:^10}|{:^10}|".format("decimal","hex","binary")]
    # print("|{:^10}|{:^10}|{:^10}|".format("decimal","hex","binary"))                                  # print column headers
    for number in range(16):
        number_format = "|{:<10d}|{:^10x}|{:>10b}|".format(number, number, number)
        # print(number_format)                                                                          # print rows as they are generated
        formatted_numbers_list.append(number_format)
    return formatted_numbers_list

# ZADANIE 10

example_text_1 = "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0."
example_text_2 = "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn"
example_word_1 = "Python"
example_word_2 = "python"

def find_word(text, word):
    matched_string = re.search(word, text)
    returned_dictionary = {
        "result" : bool(matched_string),
        "first_index": matched_string.start() if matched_string else None,
        "last_index": matched_string.end() if matched_string else None,
        "search_string": word,
        "string": text,
    }
    return returned_dictionary

# ZADANIE 11

def find_all_words(text, word):
    matched_strings = re.findall(word, text, flags = re.IGNORECASE)
    # print(matched_strings)                                                                            # print matching words list
    return matched_strings

# ZADANIE 12

example_spam_words = ["began", "Python"]

def replace_spam_words(text, spam_words):
    print("\ntext = ", text)
    print("spam_words = ", spam_words)
    return

# WYWOLANIA

if __name__ == "__main__":

    # LISTA FUNKCJI DO WYKONANIA
    
    functions_to_execute = [
        # empty_function(),                                                                             # PUSTA FUNKCJA  
        # real_len("Alex\nKdfe23\t\f\v.\r"),                                                            # ZADANIE 1
        # find_articles("Ocean", True),                                                                 # ZADANIE 2
        # sanitize_phone_number("    +38(050)123-32-34"),                                               # ZADANIE 3  
        # is_check_name("Kevin Costner", "Kevin"),                                                      # ZADANIE 4            
        # get_phone_numbers_for_countries(['380998759405', '818765347', '8867658976', '657658976'])     # ZADANIE 5     
        # is_spam_words("Copycat", ["cat"]),                                                            # ZADANIE 6 
        # is_spam_words("Copycat", ["cat"], True),
        # is_spam_words("Copy cat.", ["cat"]),
        # is_spam_words("Copy cat.", ["cat"], True), 
        # translate("Дмитрий Коробов"),                                                                 # ZADANIE 7
        # translate("Александр Иванович"),
        # formatted_grades({"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}),                      # ZADANIE 8
        # formatted_numbers(),                                                                          # ZADANIE 9
        # find_word(example_text_1, example_word_1),                                                    # ZADANIE 10
        # find_word(example_text_1, example_word_2),    
        # find_all_words(example_text_1, example_word_1),                                               # ZADANIE 11
        # find_all_words(example_text_1, example_word_2),
        replace_spam_words(example_text_2,example_spam_words)                                         # ZADANIE 12
    ]
    
    # WYKONANIE FUNKCJI I WYŚWIETLENIE WYNIKÓW
    
    if functions_to_execute:
        print()
        for single_function in functions_to_execute:
            print(f"return = {single_function}")
        print()
    else:
        print("\nWybierz funkcję z listy funkcji do wykonania.\n")