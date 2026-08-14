account_size = float(input("Account Size: "))
while account_size <= 0:
    print("Invalid Account Size.Try Again.")
    account_size = float(input("Account Size: "))
else:
    print("Account accepted.")