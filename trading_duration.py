timeframes = {
    "1m": 1,
    "5m" : 5,
    "15m" : 15,
    "1H" : 1,
    "2H" : 2,
    "4H" : 4,
    "1D" : 1,
    "1W" : 1,
    "1M" : 1
}
no_of_candles_in_trade = 8


def trade_duration():
    durarion = selected_timeframe * no_of_candles_in_trade
    return durarion
print(trade_duration())