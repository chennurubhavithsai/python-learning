website = input("Enter website to search: ").lower()

found = False

with open("passwords.txt", "r") as file:
    lines = file.readlines()

for i in range(len(lines)):
    if lines[i].startswith("Website:"):
        saved_website = lines[i].split(":")[1].strip().lower()

        if saved_website == website:
            print("\n✅ Password Found!")
            print(lines[i].strip())        # Website
            print(lines[i + 1].strip())    # Username
            print(lines[i + 2].strip())    # Password
            found = True
            break

if not found:
    print("\n❌ No password found for this website.")