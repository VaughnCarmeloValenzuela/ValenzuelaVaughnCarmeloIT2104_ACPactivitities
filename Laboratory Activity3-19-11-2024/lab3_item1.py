def roman_to_integer(value):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer_value = 0
    prev_value = 0

    for char in value[::-1]:
        value = roman_values[char.upper()]  # Convert to uppercase for lookup
        if value < prev_value:
            integer_value -= value
        else:
            integer_value += value
        prev_value = value

    return integer_value

roman_numeral = input("Enter a Roman numeral: ")
uppercase_numeral = roman_numeral.upper()
result = roman_to_integer(uppercase_numeral)
print(f"The integer value of '{uppercase_numeral}' is: {result}")