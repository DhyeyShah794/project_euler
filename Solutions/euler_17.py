"""If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
20 letters. The use of "and" when writing out numbers is in compliance with British usage."""

"""Answer is 21124"""
# My approach (convoluted mess)

hundreds_place = {
    0: " ",
    1: "one hundred ",
    2: "two hundred ",
    3: "three hundred ",
    4: "four hundred ",
    5: "five hundred ",
    6: "six hundred ",
    7: "seven hundred ",
    8: "eight hundred ",
    9: "nine hundred "
}

tens_place_1 = {
    0: "",
    1: "ten",
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
}

tens_and_units_place = {
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}

units_place_1 = {
    1: " one",
    2: " two",
    3: " three",
    4: " four",
    5: " five",
    6: " six",
    7: " seven",
    8: " eight",
    9: " nine"
}


def num_to_words(num: int):  # Could be separate functions for 2 and 3 digit numbers, but should I do it? Nah I'm fine
    if num > 1000 or num < 1:
        return ValueError
    units_digit = int(str(num)[-1])

    if num == 1000:
        return "one thousand"

    elif 1 <= num < 100:
        if 1 <= num < 10:
            num_in_words = units_place_1.get(num)
            return num_in_words
        elif num % 10 == 0:
            digit = int(str(num)[0])
            num_in_words = tens_place_1.get(digit)
            return num_in_words
        elif 10 < num < 20:
            num_in_words = tens_and_units_place.get(num)
            return num_in_words
        else:
            tens_digit = int(str(num)[0])
            num_in_words = tens_place_1.get(tens_digit) + units_place_1.get(units_digit)
            return num_in_words

    tens_digit = int(str(num)[1])
    if tens_digit == units_digit == 0:
        hundreds_digit = int(str(num)[0])
        num_in_words = hundreds_place.get(hundreds_digit)
        return num_in_words

    elif units_digit == 0 and num > 99:
        hundreds_digit = int(str(num)[0])
        tens_digit = int(str(num)[1])
        num_in_words = hundreds_place.get(hundreds_digit) + "and " + tens_place_1.get(tens_digit)
        return num_in_words

    elif units_digit != 0 and num > 99:
        hundreds_digit = int(str(num)[0])
        tens_digit = int(str(num)[1])
        tens_and_units_digits = int(str(num)[1:3])
        if 10 < tens_and_units_digits < 20:
            num_in_words = hundreds_place.get(hundreds_digit) + "and " + tens_and_units_place.get(tens_and_units_digits)
            return num_in_words
        elif tens_digit == 0:
            num_in_words = hundreds_place.get(hundreds_digit) + "and " + units_place_1.get(units_digit)
            return num_in_words
        else:
            num_in_words = hundreds_place.get(hundreds_digit) + "and " + tens_place_1.get(tens_digit)\
                           + units_place_1.get(units_digit)
            return num_in_words


def char_count(string):
    space_removed = string.replace(" ", "")
    return len(space_removed)


numbers_in_words = [char_count(num_to_words(i)) for i in range(1, 1001)]

print(sum(numbers_in_words))
