watchlist = {
    "EURUSD": {"market": "Forex", "score": 90},
    "GBPUSD": {"market": "Forex", "score": 72},
    "BTCUSD": {"market": "Crypto", "score": 91},
    "SP500": {"market": "Index", "score": 68},
    "AUDCAD": {"market": "Forex", "score": 88}
}
for pair, data in watchlist.items():
    print(pair, data)

for pair,data in watchlist.items():
    if data["score"] >= 80:
        print(pair)

for pair,data in watchlist.items():
    if data["score"] >= 80:
        data["status"] = "qualified"
    else:
        data["status"] = "rejected"
    print(pair, data)
print()

for pair,data in watchlist.items():
    if data["score"] >= 80 and data["market"] == "Forex":
        data["status"] = "qualified"
    else:
        data["status"] = "rejected"
    print(pair, data)

counter = 0
for pair,data in watchlist.items():
    if data["status"] == "qualified":
        counter += 1
print(counter)

currency = input().upper()
def pair_value(currency):
    value = None
    if currency.endswith("USD"):
        value = 10
    elif currency.endswith("JPY"):
        value = 7.12
    else:
        value = "Unknown Pair."
    return value
print(pair_value(currency))
