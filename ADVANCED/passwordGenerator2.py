import random
import string

class PasswordGenerator:
    def __init__(self, password_length, use_uppercase=True, use_lowercase=True, use_digits=True):
        self.password_length = password_length
        self.use_uppercase = use_uppercase
        self.use_lowercase = use_lowercase
        self.use_digits = use_digits

    def generate(self):
        characters = ""
        if self.use_uppercase:
            characters += string.ascii_uppercase
        if self.use_lowercase:
            characters += string.ascii_lowercase
        if self.use_digits:
            characters += string.digits

        if not characters:
            return "Error: You must select at least one type of characters to generate the password."

        self.password = "".join(random.choice(characters) for _ in range(self.password_length))

    def show(self):
        print(self.password)

    def write(self, num_of_passwords):
        with open("passwords.txt", "w") as file:
            for _ in range(num_of_passwords):
                self.generate()
                file.write(self.password + "\n")

# შემოწმების გაშვება
password_length = int(input("შეიყვანეთ პაროლის სიგრძე: "))
use_uppercase = input("გსურთ მაღალი ასოების გამოყენება? (კი/არა): ").lower() == "კი"
use_lowercase = input("გსურთ დაბალი ასოების გამოყენება? (კი/არა): ").lower() == "კი"
use_digits = input("გსურთ რიცხვების გამოყენება? (კი/არა): ").lower() == "კი"

pg = PasswordGenerator(password_length, use_uppercase, use_lowercase, use_digits)
pg.generate()
pg.show()

num_of_passwords_to_write = int(input("რაოდენობა პაროლების ჩაწერისთვის?: "))
pg.write(num_of_passwords_to_write)
