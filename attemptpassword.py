# ATTEMPT PASSWORD
attempt = 0
true_pin = "password1"

while attempt < 3:
    attempt += 1
    pin = (input("Enter your pin: "))

    if pin == true_pin:
        print("Access Granted")
        break

else:
    print("Access Denied!")

if attempt == 3 and pin != true_pin:
    print("Max attempt reached. Blocked!")