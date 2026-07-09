#Trade Validator

#Variables
currency = "AUDUSD"
bias = "long"
entry_price = 0.69371
tp_price = 0.69112
sl_price = 0.69431
reward_ratio = 3

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