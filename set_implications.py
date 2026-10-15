# # forex_pairs = {"EURUSD", "GBPUSD", "USDJPY", "AUDCAD", "EURUSD"}
# # crypto_pairs = {"BTCUSD", "ETHUSD", "SOLUSD"}
# # set_A = forex_pairs
# # set_B = crypto_pairs

# # # print(forex_pairs & crypto_pairs)
# # # print(forex_pairs | crypto_pairs)
# # # print(forex_pairs - crypto_pairs)
# # # print(forex_pairs ^ crypto_pairs)
# # # forex_pairs.add("GBPJPY")
# # # print(forex_pairs)
# # # forex_pairs.add("EURUSD")
# # # print(forex_pairs)
# # # forex_pairs.remove("GBPUSD")
# # # print(forex_pairs)
# # # forex_pairs.discard("NZDUSD")
# # # print(forex_pairs)
# # # "EURUSD" in forex_pairs
# # # "NZDUSD" in forex_pairs
# # currency_pair = input("Enter a currency pair: ").upper().strip()
# # currency_pair =  currency_pair.replace(" ", "")
# # if currency_pair in forex_pairs:
# #     print("Pair found")
# # else:

# #     print("Pair not found")

# morning_watchlist = {"EURUSD", "GBPUSD", "AUDCAD"}
# evening_watchlist = {"EURUSD", "USDJPY", "GBPJPY"}
# both = morning_watchlist & evening_watchlist
# print(both)
# morning_only = morning_watchlist - evening_watchlist
# print(morning_only)
# unique_pairs = morning_watchlist ^ evening_watchlist
# print(unique_pairs)
forex_pairs = {"EURUSD", "GBPUSD", "USDJPY", "AUDCAD", "NZDUSD"}


while True:
    currency_pair = "".join(input("Input a pair symbol: ").upper().strip().split())

    if currency_pair in forex_pairs:
        print("Pair approved")
        break
    elif currency_pair == "":
        print("Enter a currency pair")
    else:
        print("Pair not approved")
