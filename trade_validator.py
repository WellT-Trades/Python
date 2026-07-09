#Trade Validator

#Variables

currency = input("Currency: ").upper()
bias = input("Bias (long/short): ").lower()
entry_price = float(input("Entry Price: "))
tp_price = float(input("TP Price: "))
sl_price = float(input("SL Price: "))
reward_ratio = float(input("RR: "))

# #Bias Validity
# if bias == "long":
#     if tp_price > entry_price:
#         print("Valid long trade.")
#     else:
#         print("Invalid TP for a long trade.")
# elif bias == "short":
#     if tp_price < entry_price:
#         print("Valid short trade.")
#     else:
#         print("Invalid TP for a short trade.")
# else:
#     print("Invalid bias.")

# #Validate the reward ratio.
# if reward_ratio < 2:
#     print("Trade rejected.\nReward-to-Risk ratio is below 2:1.")
# else:
#     print("Trade accepted.")
if (
    (bias == "short" and tp_price < entry_price)
    or
    (bias == "long" and tp_price > entry_price)
)and reward_ratio >= 2:
    print("Trade accepted.")
else:
    print("Trade rejected.")

print("\n===Trade Summary===")
print("\nCurrency:", currency)
print("Bias:", bias)
print("Entry:", entry_price)
print("TP:", tp_price)
print("SL:", sl_price)
print("RR:", reward_ratio)
