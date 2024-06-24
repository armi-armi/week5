def extract_name(email):
    parts = email.split('@')[0].split('.')
    return " ".join(parts).title()

emails = {}
email = input("Email: ")

while email != "":
    name = extract_name(email)
    is_name_correct = input(f"Is your name {name}? (Y/n) ").lower()
    if is_name_correct == 'n':
        name = input("Name: ")
    emails[email] = name
    email = input("Email: ")

for email, name in emails.items():
    print(f"{name} ({email})")
