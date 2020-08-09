# Validate: https://suspha.github.io/numerology/
# Regex generator: https://www.regexpal.com/93828
# Sum of digits: https://www.geeksforgeeks.org/finding-sum-of-digits-of-a-number-until-sum-becomes-single-digit/

from num_utils import *
import re

dob_regex = "^(0[1-9]|[12][0-9]|3[01])[/](0[1-9]|1[012])[/](19|20)\d\d$"


def input_dob():
    # input date of birth
    # test values: 02/11/1988 | 22/11/1988
    dob = input("\nEnter your date of birth (DD/MM/YYYY): ")
    # validate dob format
    while not re.match(dob_regex, dob):
        print("Please follow the format!")
        dob = input("Enter your date of birth (DD/MM/YYYY): ")
    # confirm dob
    day, month, year = [int(x) for x in dob.split("/")]
    return day, month, year


def input_current_name():
    # input current name
    # test values: Claudia Miulescu
    current_name = input("Enter your current name (FirstName LastName): ")
    # validate name format
    while len(current_name) < 3:
        print("Please follow the format!")
        current_name = input("Enter your current name (FirstName LastName): ")
    # format current name
    current_names = current_name.upper().split(" ")
    return current_names


def input_official_name():
    # input official name
    # test values: Claudia Alina Miulescu
    official_name = input("Enter your official name (FirstName MiddleName LastName): ")
    # validate name format
    while len(official_name) < 3:
        print("Please follow the format!")
        official_name = input("Enter your official name (FirstName MiddleName LastName): ")
    # format official name
    official_names = official_name.upper().split(" ")
    return official_names


def main():
    print("Welcome! Here you can calculate your Numerology Profile..")

    day, month, year = input_dob()
    current_names = input_current_name()
    official_names = input_official_name()

    print("DoB Day: ", day, " Month: ", month, " Year: ", year)
    print("Current Name: ", ' '.join(current_names))
    print("Official Name: ", ' '.join(official_names))

    # 1. calculate_birthday_numbers
    birthday_numbers = calculate_birthday_numbers(day)
    print("\nYour Birthday Number: ", birthday_numbers[-1])
    if len(birthday_numbers) > 1:
        print("All Birthday Numbers: ", '/'.join(str(x) for x in birthday_numbers))

    # 2. calculate_life_path_number
    life_path_number = calculate_life_path_number(day, month, year)
    print("Your Life Path Number: ", life_path_number)


    print("\n\nYour Profile in Chaldean System\n")

    # 3. calculate_current_name_number with chaldean_framework
    chaldean_current_name_number = calculate_name_number(current_names, chaldean_framework)
    print("Your Chaldean Current Name Number: ", chaldean_current_name_number)

    # 4. calculate_personality_number with chaldean_framework
    chaldean_personality_number = calculate_personality_number(current_names, chaldean_framework)
    print("Your Chaldean Personality Number: ", chaldean_personality_number)

    # 5. calculate_soul_number with chaldean_framework
    chaldean_soul_number = calculate_soul_number(current_names, chaldean_framework)
    print("Your Chaldean Soul Number: ", chaldean_soul_number)

    # 6. calculate_destiny_number with chaldean_framework
    chaldean_destiny_number = calculate_name_number(official_names, chaldean_framework)
    print("Your Chaldean Destiny Number: ", chaldean_destiny_number)

    # 7. calculate_maturity_number with chaldean_framework
    chaldean_maturity_number = chaldean_destiny_number + life_path_number
    print("Your Chaldean Maturity Number: ", chaldean_maturity_number)


    print("\n\nYour Profile in Pythagorean System\n")

    # 3'. calculate_current_name_number with pythagorean_framework
    pythagorean_current_name_number = calculate_name_number(current_names, pythagorean_framework)
    print("Your Pythagorean Current Name Number: ", pythagorean_current_name_number)

    # 4'. calculate_personality_number with pythagorean_framework
    pythagorean_personality_number = calculate_personality_number(current_names, pythagorean_framework)
    print("Your Pythagorean Personality Number: ", pythagorean_personality_number)

    # 5'. calculate_soul_number with pythagorean_framework
    pythagorean_soul_number = calculate_soul_number(current_names, pythagorean_framework)
    print("Your Pythagorean Soul Number: ", pythagorean_soul_number)

    # 6'. calculate_destiny_number with pythagorean_framework
    pythagorean_destiny_number = calculate_name_number(official_names, pythagorean_framework)
    print("Your Pythagorean Destiny Number: ", pythagorean_destiny_number)

    # 7'. calculate_maturity_number with pythagorean_framework
    pythagorean_maturity_number = pythagorean_destiny_number + life_path_number
    print("Your Pythagorean Maturity Number: ", pythagorean_maturity_number)


if __name__ == "__main__":
    main()
