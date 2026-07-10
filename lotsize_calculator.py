# LOTSIZE CALCULATOR
account_size = float(input("Account Size: "))
currency = input("Currency: ").upper()
risk_percentage = float(input("Risk(%): "))
sl_pips = float(input("SL Pips: "))
pair_value = float(input("Pair Value: "))

# CONVERSIONS
risk_amount = (risk_percentage / 100) * account_size
risk_percentage = (risk_amount / account_size) * 100

# FORMULA
lot_size = (risk_amount / sl_pips) / pair_value

print("\n=== SUMMARY===")
print("Currency:", currency)
print("SL:", sl_pips)
print("Risk (%):", risk_percentage)
print("Risk Amount:", risk_amount)

print(f"Lot size: {lot_size:.2f}")
