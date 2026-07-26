import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password

website = input("Enter website name: ")
username = input("Enter username/email: ")

length = int(input("Enter password length: "))
password = generate_password(length)

print("\nGenerated Password:", password)

with open("passwords.txt", "a") as file:
    file.write(f"Website: {website}\n")
    file.write(f"Username: {username}\n")
    file.write(f"Password: {password}\n")
    file.write("-----------------------------\n")

print("\n✅ Password saved successfully!")