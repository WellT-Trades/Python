#Profit Calculator

# Variables
currency = "AUDUSD"
bias = "short"
entry_price = 0.69371
TP_price = 0.69112 #(TP means Take Profit)
SL_price = 0.69431 #(SL means stop loss)
lot_size = 0.83

# Calculate Profit = (Exit Price − Entry Price) × Lot Size
Profit = (TP_price - entry_price) * lot_size

# Output
print(currency, bias)
print("Profit:", Profit)
