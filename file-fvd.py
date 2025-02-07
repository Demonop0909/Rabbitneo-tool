import requests
import random
import string

def generate_code(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def check_code(code):
    url = f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return True
    else:
        return False

def generate_and_check_codes(count, nitro=True):
    codes = []
    for _ in range(count):
        code = generate_code(16 if nitro else 24)
        if check_code(code):
            codes.append(code)
    return codes

# Generate 10 nitro codes
nitro_codes = generate_and_check_codes(10)
print(f'Generated {len(nitro_codes)} nitro codes:')
for code in nitro_codes:
    print(code)

# Generate 10 boost codes
boost_codes = generate_and_check_codes(10, nitro=False)
print(f'\nGenerated {len(boost_codes)} boost codes:')
for code in boost_codes:
    print(code)