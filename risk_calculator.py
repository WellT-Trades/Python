# # Without looking anything up, write a Python program that:
# Creates a variable called account_size and stores 1000.
# Creates a variable called risk_percent and stores 2.
# Calculates the risk amount using:
# Risk Amount = Account Size × Risk Percent ÷ 100
# Stores the result in a variable called risk_amount.
# Prints:
# Account Size: 1000
# Risk Percent: 2
# Risk Amount: 20

account_size = 1000
risk_percent = 5

# Calculates the risk amount
risk_amount = account_size * risk_percent / 100

if risk_percent > 2:
    print("\nWarning: Risk exceeds your trading plan.")

else:
    print("\nRisk is within your trading plan.\n")

print("Account Size:", account_size,  "\n")
print("Risk Percent:", risk_percent, "\n")
print("Risk Amount:",  risk_amount, "\n")