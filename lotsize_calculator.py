# LOTSIZE CALCULATOR
account_size = float(input("Account Size: "))
currency = input("Currency: ").upper()
risk_percentage = float(input("Risk(%): "))
sl_pips = float(input("SL Pips: "))
pair_value = float(input("Pair Value: "))


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
     risk_amount = (risk_percentage / 100) * account_size

    # LOT SIZE FORMULA
     lot_size = (risk_amount / sl_pips) / pair_value
     
     print("\n=== SUMMARY===")
     print("Currency:", currency)
     print("SL:", sl_pips)
     print("Risk (%):", risk_percentage)
     print("Risk Amount:", risk_amount)
     print(f"Lot size: {lot_size:.2f}")