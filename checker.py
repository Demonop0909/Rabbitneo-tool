import re

def is_valid_nitro(code):
    nitro_pattern = r"^[a-zA-Z0-9]{24}\.[a-zA-Z0-9]{6}\.[a-zA-Z0-9]{27}$"
    return re.match(nitro_pattern, code) is not None

def check_nitro_codes(file_path):
    valid_codes = []
    invalid_codes = []

    with open(file_path, 'r') as file:
        for line in file:
            code = line.strip()
            if is_valid_nitro(code):
                valid_codes.append(code)
            else:
                invalid_codes.append(code)

    return valid_codes, invalid_codes

# Usage example
file_path = 'nitro_codes.txt'
valid_codes, invalid_codes = check_nitro_codes(file_path)

print("Valid Nitro Codes:")
for code in valid_codes:
    print(code)

print("\nInvalid Nitro Codes:")
for code in invalid_codes:
    print(code)