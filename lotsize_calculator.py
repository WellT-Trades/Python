# LOTSIZE CALCULATOR
account_size = 5000
currency = "AUDUSD"
risk_percentage = 1
risk_amount = 50
sl_pips = 5.5
pair_value = 10

# CONVERSIONS
risk_amount = (risk_percentage / 100) * account_size
risk_percentage = (risk_amount / account_size) * 100

# FORMULA
lot_size = (risk_amount / sl_pips) / pair_value
print(lot_size)
