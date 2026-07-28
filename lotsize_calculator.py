# LOTSIZE CALCULATOR

# IMPORTS
from risk_calculator import calculate_risk_percent
# FUNCTIONS
def calculate_lot_size(risk_amount, sl_pips, pair_value):
    lot_size = (risk_amount / sl_pips) / pair_value
    return lot_size

def format_summary(currency, account_size, sl_pips, risk_percentage, risk_amount, lot_size):
    summary = (f"{'=' * 20}\nTRADE  SUMMARY\n{'=' * 20}\nAccount Size: {account_size}\nCurrency: {currency}\nSL: {sl_pips}\nRisk (%): {risk_percentage}% of {account_size}\nRisk Amount: {risk_amount}\nLot size: {lot_size:.2f}\n")
    return(summary)


if __name__ == "__main__":
    # INPUTS
    account_size = float(input("Account Size: "))
    currency = input("Currency: ").upper()
    risk_amount = float(input("Risk Amount: "))
    sl_pips = float(input("SL Pips: "))
    pair_value = float(input("Pair Value: "))

    # CONDITIONS
    while account_size <= 9:
        print("\nError!: Trader must have capital.")
        account_size = float(input("Account Size: "))

    while risk_amount <= 0:
        print("\nError!: Risk must be greater than zero.")
        risk_amount = float(input("Risk Amount: "))

    while sl_pips <= 1:
        print("\nError!: SL must be greater than one.")
        sl_pips = float(input("SL Pips: "))

    while pair_value <= 0:
        print("\nError!: Pair value must be greater than zero")
        pair_value = float(input("Pair Value: "))

    else:
        # CONVERSIONS
        # RISK AMOUNT FORMULA
        risk_percent = int(calculate_risk_percent(
            account_size,
            risk_amount
            ))
        
        # LOT SIZE FORMULA
        lot_size = calculate_lot_size(
            risk_amount,
            sl_pips,
            pair_value
        )
        # SUMMARY OUTPUT
        summary = format_summary(
            currency,
            account_size,
            sl_pips,
            risk_percent,
            risk_amount,
            lot_size
        )
        
print(summary)
        