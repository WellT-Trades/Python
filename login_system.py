correct_username = "admin"
correct_password = 1234
username_attempts = 4
password_attempts = 4

while username_attempts > 0:
    username_attempts -= 1
    username = input("Enter username: ")
    username = username.strip().lower()
    if username == correct_username:
        break
    else:
        print("Incorrect username.Try again.")
else:
    print("Account locked.")
    exit()
while password_attempts > 0:
    
    try:
        password = int(input("Enter password: "))
    except ValueError:
        print("Invalid input. Try again")
        continue
    password_attempts -= 1
    if password == correct_password:
        print("Login successful!")
        exit()
    else:
        print("Incorrect password.Try again.")
else:
    print("Account locked.")