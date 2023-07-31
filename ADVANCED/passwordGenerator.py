import random
import string

def generate_password(password_length, use_uppercase, use_lowercase, use_digits):
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits

    if not characters:
        return "Error: You must select at least one type of characters to generate the password."

    password = "".join(random.choice(characters) for _ in range(password_length))
    return password

# შემოწმების გაშვება
password_length = int(input("შეიყვანეთ პაროლის სიგრძე: "))
use_uppercase = input("გსურთ მაღალი ასოების გამოყენება? (კი/არა): ").lower() == "კი"
use_lowercase = input("გსურთ დაბალი ასოების გამოყენება? (კი/არა): ").lower() == "კი"
use_digits = input("გსურთ რიცხვების გამოყენება? (კი/არა): ").lower() == "კი"

generated_password = generate_password(password_length, use_uppercase, use_lowercase, use_digits)
print("შემოიყვანეთ ფარგლებში: ", generated_password)
