import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    if not (use_upper or use_lower or use_digits or use_special):
        raise ValueError("At least one character set must be selected!")

    character_pool = ''
    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation

    if length < 1:
        raise ValueError("Password length must be at least 1.")

    # Ensure the password has at least one character from each selected set
    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))

    remaining_length = length - len(password)
    password += random.choices(character_pool, k=remaining_length)

    random.shuffle(password)
    return ''.join(password)

# Example usage
if _name_ == "_main_":
    try:
        pwd = generate_password(length=16, use_upper=True, use_lower=True, use_digits=True, use_special=True)
        print("Generated Password:", pwd)
    except ValueError as e:
        print("Error:", e)