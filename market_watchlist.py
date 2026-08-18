# MARKET WATCHLIST

watchlist = [
    "EURUSD",

    "GBPUSD",

    "USDJPY",

    "XAUUSD"
]

print(watchlist)


user_input = input("Enter 1 to add pair, 2 to remove, 3 to pop, 4 to view watchlist, 0 to exit.\n")

# def watchlist_manager(option):
#     if c == 1:
#     elif user_input == "2":

#         pair = input("Enter pair")
#         if pair in watchlist:
                
#             watchlist.remove(pair)
#         else:
#             print("The item does not exist in the list")

#     elif user_input == "3":
#         pop_position = int(input("Enter the position you want to pop item"))
#         if pop_position > len(watchlist) or pop_position < 1:
#             print("The position is out of range")
#             return
#         else:
#             popped_item = watchlist.pop(pop_position - 1 )
#             return popped_item

        

# # new_pair = input("Enter pair: ").upper()
# # if new_pair in watchlist:
# #     print(f"{new_pair} is already in watchlist. Take a look.\n\n")
# # else:
# #     watchlist.append(new_pair)

# # if new_pair not in watchlist:
#     # print(f"{new_pair} not found on watchlist.. View watchlist.\n\n")
# # else:
#     # watchlist.remove(new_pair)

# exempt_pair = watchlist.pop()
# print(f"{exempt_pair} has been removed from your watchlist.")

# print(f"{'=' * 20}\n{' ' * 2}TRADE WATCHLIST\n{'=' * 20}")

# for index in range(len(watchlist)):
#     print(
#         f"{index + 1}. {watchlist[index]}"
#     )


def add_item(new_pair):
    watchlist.append(new_pair)
    print(f"{new_pair} successfully added to your watchlist.")
    return

def removed_item(pair):
    watchlist.remove(pair)
    print(f"{pair} has successfully been removed from your watchlist.")
    return

def pop_item(pop_position):
    index = pop_position -1
    popped_item = watchlist.pop(index)
    print(f"Loading popped item...\n{popped_item}")
    return

def view_watchlist(watchlist):
    print(watchlist)
    return


if user_input == "1":
    new_pair = input("Enter the symbol: ").upper()
    if new_pair in watchlist:
        print(f"{new_pair} already exists in watchlist.")
    else:
        add_item(new_pair)

elif user_input == "2":
    pair = input("Enter the symbol: ").upper()
    if pair not in watchlist:
        print(f"Error! {pair} not in watchlist.")
    else:
        removed_item(pair)

elif user_input == "3":
    pop_position = int(input("Enter the position of symbol: "))
    if pop_position > len(watchlist) or pop_position < 1:
        print(f"Range is out of bound! View watchlist.")
    else:
        pop_item(pop_position)
        

elif user_input == "4":
    view_watchlist(watchlist)

else:
    if user_input == "0":
        print("Watchlist closed.")
        exit
    else:
        print(f"Invalid or No selection.\n{'=' * 20}\n{' ' * 2}TRADE WATCHLIST\n{'=' * 20}\n{index + 1}. {watchlist[index]}")
        exit