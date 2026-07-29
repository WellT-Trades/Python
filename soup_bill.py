    # ITEM List
Meat = 4000
Stockfish = 1000
Dryfish = 2000
Isam = 1000
Canda = 1000
Uziza_leaf = 200
Oha_leaf = 200
Ofor = 500 #(thickener)
Onion_and_Pepper = 1000

def item_list():
    item = ''' 
===== Native Soup List =====
Meat = 4000
Stockfish = 1000
Dryfish = 2000
Isam = 1000
Canda = 1000
Uziza_leaf = 200
Oha_leaf = 200
Ofor = 500 #(thickener)
Onion_and_Pepper = 1000
    '''
    return item

def sum_total():
    total = (Meat + Stockfish + Dryfish + Isam + Canda + Uziza_leaf + Oha_leaf + Ofor + Onion_and_Pepper)
    return total

def investors_share():
    number_of_investors = 4
    shares = sum_total() / number_of_investors
    return int(shares)

def go_fund_native_soup():
    account = '''8182538967
                 Palmpay
                 WellT
    '''
    return account

def beneficiaries():
    names_of_beneficiaries = '''1. WellT
                        2. LMG
                        3. VICK
                        4. LIZZY
'''
    return names_of_beneficiaries

def summary_report():
    summary = f''' 
{item_list()}
Total: {sum_total()} NGN\n
Investors Share: {investors_share()} NGN\n
Account Details: {go_fund_native_soup()}
Names of Beneficiaries: {beneficiaries()}
'''
    return summary
print(summary_report())