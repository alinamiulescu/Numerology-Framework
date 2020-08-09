
from num_framework import *


# find sum of digits of a number until sum becomes single digit
def calc_sum_of_digits(n):
    if n == 0:
        return 0
    if n % 9 == 0:
        return 9
    else:
        return n % 9


def calc_sum_of_digits_with_memory(n):
    sum_dig = 0
    sum_array = []

    while n > 0 or sum_dig > 9:
        if n == 0:
            n = sum_dig
            sum_dig = 0

        sum_dig += int(n % 10)
        n /= 10

        if n == 0:
            sum_array.append(sum_dig)

    return sum_array


def calculate_birthday_numbers(day):
    # birthday_number = calc_sum_of_digits(day)
    # return birthday_number
    birthday_numbers = calc_sum_of_digits_with_memory(day)
    return birthday_numbers


def calculate_life_path_number(day, month, year):
    d = calc_sum_of_digits(day)
    m = calc_sum_of_digits(month)
    y = calc_sum_of_digits(year)
    s = d + m + y
    life_path_number = calc_sum_of_digits(s)
    return life_path_number


def calc_sum_of_name(name, framework):
    sum_name = 0
    for c in name:
        sum_name += framework.get(c)
    return sum_name


def eliminate_consonants(name):
    return ''.join(c for c in name if c in vowels)


def eliminate_vowels(name):
    return ''.join(c for c in name if c not in vowels)


def calculate_name_number(names, framework):
    overall_sum = 0
    for name in names:
        name_sum = calc_sum_of_name(name, framework)
        # print("FINAL name: ", name)
        # print("FINAL name_sum: ", name_sum)
        overall_sum += name_sum
        # overall_sum += calc_sum_of_digits(name_sum) --> TODO: verify if each name has to be reduced to one digit sum

    # print("FINAL overall_sum: ", overall_sum)
    name_number = calc_sum_of_digits(overall_sum)
    # print("FINAL name_number: ", name_number)

    return name_number


def calculate_personality_number(names, framework):
    personality_sum = 0
    for name in names:
        name_w_consonants = eliminate_vowels(name)
        name_sum = calc_sum_of_name(name_w_consonants, framework)
        # personality_sum += name_sum --> bring each name to one digit sum first and then add
        personality_sum += calc_sum_of_digits(name_sum)
    # print("FINAL personality_sum: ", personality_sum)

    personality_number = calc_sum_of_digits(personality_sum)
    # print("FINAL personality_number: ", personality_number)
    return personality_number


def calculate_soul_number(names, framework):
    soul_sum = 0
    for name in names:
        name_w_vowels = eliminate_consonants(name)
        name_sum = calc_sum_of_name(name_w_vowels, framework)
        # soul_sum += name_sum --> bring each name to one digit sum first and then add
        soul_sum += calc_sum_of_digits(name_sum)
    # print("FINAL soul_sum: ", soul_sum)

    soul_number = calc_sum_of_digits(soul_sum)
    # print("FINAL personality_number: ", soul_number)
    return soul_number

