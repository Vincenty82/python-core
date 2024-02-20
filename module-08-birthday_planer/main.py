### IMPORT ###

from datetime import datetime

### VARIABLES ###

users = [
    {"name": "Jan", "birthday": datetime(2024, 2, 19)},
    {"name": "Anna", "birthday": datetime(2024, 2, 20)},
    {"name": "Piotr", "birthday": datetime(2024, 2, 21)},
    {"name": "Katarzyna", "birthday": datetime(2024, 2, 21)},
    {"name": "Andrzej", "birthday": datetime(2024, 2, 23)},
    {"name": "Agnieszka", "birthday": datetime(2024, 2, 24)},
    {"name": "Tomasz", "birthday": datetime(2024, 2, 24)},
    {"name": "Zuzanna", "birthday": datetime(2024, 2, 25)},
    {"name": "Marek", "birthday": datetime(2024, 2, 25)},
    {"name": "Magdalena", "birthday": datetime(2024, 2, 25)},
    {"name": "Paweł", "birthday": datetime(2024, 2, 27)},
    {"name": "Barbara", "birthday": datetime(2024, 2, 27)},
    {"name": "Michał", "birthday": datetime(2024, 2, 28)},
    {"name": "Ewa", "birthday": datetime(2024, 2, 29)},
    {"name": "Krzysztof", "birthday": datetime(2024, 2, 29)},
    {"name": "Marta", "birthday": datetime(2024, 3, 1)},
    {"name": "Robert", "birthday": datetime(2024, 3, 2)},
    {"name": "Karolina", "birthday": datetime(2024, 3, 2)},
    {"name": "Marcin", "birthday": datetime(2024, 3, 3)},
    {"name": "Joanna", "birthday": datetime(2024, 3, 4)},
]

### FUNCTIONS ###

def get_birthdays_per_week(users):
    for user in users:
        print(user["name"] + " " + user["birthday"].date().strftime('%Y-%m-%d'))

### MAIN ###

if __name__ == "__main__":
    get_birthdays_per_week(users)