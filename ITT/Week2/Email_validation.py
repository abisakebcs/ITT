email = input("Enter Email ID: ")

at_count = 0
dot_after_at = False

for ch in email:
    if ch == ' ':
        print("Invalid Email ID")
        exit()
    if ch == '@':
        at_count += 1
    if ch == '.' and at_count == 1:
        dot_after_at = True

if (at_count == 1 and
    email[0] != '@' and
    email[-1] != '.' and
    dot_after_at):
    print("Valid Email ID")
else:
    print("Invalid Email ID")
