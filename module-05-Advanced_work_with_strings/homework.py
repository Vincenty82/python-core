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
    return

# WYWOLANIA

if __name__ == "__main__":

    # LISTA FUNKCJI DO WYKONANIA
    
    functions_to_execute = [
        empty_function(),                                       # PUSTA FUNKCJA  
        # real_len("Alex\nKdfe23\t\f\v.\r"),                      # ZADANIE 1
        # find_articles(),                                        # ZADANIE 2
    ]
    
    # WYKONANIE FUNKCJI I WYŚWIETLENIE WYNIKÓW
    
    for single_function in functions_to_execute:
        print(f"return = {single_function}")