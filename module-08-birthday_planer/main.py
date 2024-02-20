### IMPORT ###

from datetime import datetime, timedelta

### VARIABLES ###

users = [
    {"name": "Jan", "birthday": datetime(1982, 2, 19)},
    {"name": "Anna", "birthday": datetime(1986, 2, 20)},
    {"name": "Piotr", "birthday": datetime(1996, 2, 21)},
    {"name": "Katarzyna", "birthday": datetime(1974, 2, 21)},
    {"name": "Andrzej", "birthday": datetime(1982, 2, 23)},
    {"name": "Agnieszka", "birthday": datetime(1999, 2, 24)},
    {"name": "Tomasz", "birthday": datetime(1982, 2, 24)},
    {"name": "Zuzanna", "birthday": datetime(2002, 2, 25)},
    {"name": "Marek", "birthday": datetime(1975, 2, 25)},
    {"name": "Magdalena", "birthday": datetime(2005, 2, 25)},
    {"name": "Paweł", "birthday": datetime(2006, 2, 27)},
    {"name": "Barbara", "birthday": datetime(2001, 2, 27)},
    {"name": "Michał", "birthday": datetime(1993, 2, 28)},
    {"name": "Ewa", "birthday": datetime(1989, 2, 28)},
    {"name": "Krzysztof", "birthday": datetime(2000, 2, 29)},
    {"name": "Marta", "birthday": datetime(1998, 3, 1)},
    {"name": "Robert", "birthday": datetime(1984, 3, 2)},
    {"name": "Karolina", "birthday": datetime(2003, 3, 2)},
    {"name": "Marcin", "birthday": datetime(2000, 3, 3)},
    {"name": "Joanna", "birthday": datetime(1955, 3, 4)},
]

### FUNCTIONS ###

def populate_birthdays_dictionary(users, date_range_start, date_range_end, birthdays_in_next_days):               # Function that iterates users list and assigns names to day numbers in given range. It returns populated dictionary.
    for user in users:
        try:
            date_user_upcoming_birthday = user["birthday"].replace(year=date_range_start.year).date()
        except ValueError:                                                                                          # for unlucky few that have their birthday on the February 29th
            date_user_upcoming_birthday = user["birthday"].replace(year=date_range_start.year, day=28).date()
        if date_range_start <= date_user_upcoming_birthday <= date_range_end:                                       # Check if the user birthday is in desired range
            day_number_from_today = (date_user_upcoming_birthday - date_range_start).days
            if date_user_upcoming_birthday.weekday() >=5:
                day_number_from_today = day_number_from_today + (7-date_user_upcoming_birthday.weekday())           # Birthdays on weekends are pushed to Monday
            birthdays_in_next_days[day_number_from_today].append(user["name"])                                      # Append names to days
    
    return birthdays_in_next_days

def print_upcoming_birthdays(date_range_start, date_days_range, birthdays_in_next_days):                          # Function that iterates over the dates in given range and prints upcoming birthdays from the dictionary. 
    for day_number in range(date_days_range + 1):
        if birthdays_in_next_days[day_number]:                                                                      # If day not empty print names
            day_of_week = (date_range_start + timedelta(days=day_number)).strftime("%A")
            print(f"{day_of_week}: {', '.join(birthdays_in_next_days[day_number])}")

def get_birthdays_per_week(users, date_days_range=7):                                                             # Main function that accepts users dictionary and sets default range to 7 days.
    date_range_start = datetime.now().date()                                                                        # Set the start date of the range as todays day
    date_range_end = date_range_start + timedelta(days=date_days_range)                                             # Set the end date of the range based on start and given range
    birthdays_in_next_days = {day_number: [] for day_number in range(date_days_range + 3)}                          # Create empty dictionary of upcoming birthdays based on given range
    populate_birthdays_dictionary(users, date_range_start, date_range_end, birthdays_in_next_days)                  # Populate the upcoming birthdays dictionary based on range and users data set
    print_upcoming_birthdays(date_range_start, date_days_range, birthdays_in_next_days)                             # Print populated dictionary

### MAIN ###

if __name__ == "__main__":
    get_birthdays_per_week(users)                                                                                 # Script is ready to be distributed as package
