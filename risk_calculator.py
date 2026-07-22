# RISK CALCULATOR AND VALIDATOR


# Calculates the risk percent
def calculate_risk_percent(account_size, risk_amount):
    risk_percent = (risk_amount * 100) / account_size
    return risk_percent

# print("Account Size:", account_size,  "\n")
# print("Risk Percent:", risk_percent, "\n")
if __name__ == "__main__":

    account_size = float(input("Account Size: "))
    if account_size < 10:
       print("Go get funded Trader!")
       exit()

    else:
        risk_amount = float(input("Risk amount: "))
    
    risk_percent = calculate_risk_percent(account_size, risk_amount)
    if risk_percent > 2:
        print("\nWarning: Risk exceeds trading plan.")
    else:
     print("\nRisk is within trading plan.\n")

    print(f"Risk (%): {risk_percent:.2f}%")