#Profit Calculator

# Variables
currency = "AUDUSD"
bias = "short"
entry_price = 0.69371
tp_price = 0.69112 #(TP means Take Profit)
sl_price = 0.69431 #(SL means stop loss)
lot_size = 0.83

# Calculate Profit = (Exit Price − Entry Price) × Lot Size

# Conditional Operation
if bias == "short":
    profit = (entry_price - tp_price) * lot_size

elif bias == "long":
    profit = (tp_price - entry_price) * lot_size

else:
    print("Invalid bias.")

# Output
print("Currency:", currency)
print("Bias:", bias)
print("Profit:", profit)
