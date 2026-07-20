# LOTSIZE CALCULATOR
account_size = float(input("Account Size: "))
currency = input("Currency: ").upper()
risk_percentage = float(input("Risk(%): "))
sl_pips = float(input("SL Pips: "))
pair_value = float(input("Pair Value: "))


from risk_calculator import calculate_risk

def format_summary(currency, account_size, sl_pips, risk_percentage, risk_amount, lot_size):
    summary = (f"\n=== TRADE  SUMMARY ===\n Account Size: {account_size}\n Currency: {currency}\n SL: {sl_pips}\n Risk (%): {risk_percentage}% of {account_size}\n Risk Amount: {risk_amount}\n Lot size: {lot_size:.2f}\n")
    return(summary)

# CONDITIONS
if account_size <= 0:
    print("\nError!: Trader must have capital.")

elif risk_percentage <= 0:
    print("\nError!: Risk must be greater than zero.")

elif sl_pips <= 1:
    print("\nError!: SL must be greater than one.")

elif pair_value <= 0:
    print("\nError!: Pair value must be greater than zero")

else:
    # CONVERSIONS
    risk_amount = calculate_risk(account_size, risk_percentage)

    # LOT SIZE FORMULA
    lot_size = (risk_amount / sl_pips) / pair_value
     
    print(format_summary(currency, account_size, sl_pips, risk_percentage,risk_amount, lot_size))