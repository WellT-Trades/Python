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
    from risk_calculator import calculate_risk
    risk_amount = calculate_risk(account_size, risk_percentage)
    # LOT SIZE FORMULA
    lot_size = (risk_amount / sl_pips) / pair_value
     
    print("\n=== SUMMARY===")
    print(f"Currency:{currency}")
    print(f"SL:{sl_pips}")
    print(f"Risk (%):{risk_percentage}")
    print(f"Risk Amount:{risk_amount}")
    print(f"Lot size:{lot_size:.2f}")