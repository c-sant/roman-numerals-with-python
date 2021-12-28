ROMAN_NUMERALS = {
    'I': 1,
    'IV': 4,
    'V': 5,
    'IX': 9,
    'X': 10,
    'L': 50,
    'XL': 40,
    'XC': 90,
    'C': 100,
    'CD': 400,
    'D': 500,
    'CM': 900,
    'M': 1000
}

def roman_to_int(roman_num: str):
    """
    Converts Roman numerals to integers.
    """
    roman_num = roman_num.upper()

    total = 0

    i = 0
    while i < len(roman_num):
        if roman_num[i:i + 2] in ('IV', 'IX', 'XL', 'XC', 'CD', 'CM'):
            current_num = roman_num[i:i + 2]   
            i += 2
        else:
            current_num = roman_num[i]
            i += 1
        
        total += ROMAN_NUMERALS[current_num]
    return total

def int_to_roman(value: int):
    """
    Converts integers to Roman numerals.
    """
    numerals = dict(zip(ROMAN_NUMERALS.values(), ROMAN_NUMERALS.keys()))
    roman_num = ""

    for i in sorted(numerals.keys(), reverse=True):
        n = value // i # amount of times inserted number can be divided by i
        value -= i * n
        roman_num += numerals[i] * n

    return roman_num