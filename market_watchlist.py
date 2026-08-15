# MARKET WATCHLIST
watchlist = [
    "EURUSD",

    "GBPUSD",

    "USDJPY",

    "XAUUSD",

    "AUDUSD"
]
print(f"{'=' * 20}\n{" " * 2}TRADE WATCHLIST\n{'=' * 20}")

for pair in range(len(watchlist)):
    print(
        f"{pair + 1}. {watchlist[pair]}"
    )
