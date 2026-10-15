# # # watchlist = [
# # #     ("EURUSD", "Forex", 85),
# # #     ("GBPUSD", "Forex", 72),
# # #     ("BTCUSD", "Crypto", 91),
# # #     ("SP500", "Index", 68),
# # #     ("AUDCAD", "Forex", 88)
# # # ]

# # # for pair in watchlist:
# # #     score = pair[2]
# # #     if score >= 80:
# # #         print(f"{pair[0]}, {pair[1]}, {score}")
# # watchlist = {
# #     "EURUSD": {"market": "Forex", "score": 90},
# #     "GBPUSD": {"market": "Forex", "score": 72},
# #     "BTCUSD": {"market": "Crypto", "score": 91},
# #     "SP500": {"market": "Index", "score": 68},
# #     "AUDCAD": {"market": "Forex", "score": 88}
# # }
# # # for pair, data in watchlist.items():
# # #     if data["score"] >= 80:
# # #         data["status"] = "qualified"
# # #         print(f"{pair} {data['score']}, {data["market"]},{data["status"]}")
# # for pair in watchlist.items():
# #     print(pair)
# # # watchlist["EURUSD"]["status"] = "active"
# # # print(watchlist["EURUSD"])
# # LIST COMPREHENSION
# # scores = [90, 72, 88, 65, 95, 78, 84]
# # highscores = [score for score in scores if score >= 80]
# # print(highscores)
# # numbers = [2, 4, 6, 8]
# # squared = [number ** 2 for number in numbers]
# # print(squared)
# # DICTIONARY COMPREHENSION
# # scores = {
# #     "John": 85,
# #     "Mary": 72,
# #     "Peter": 90,
# #     "Jane": 65
# # }
# # highscores ={student : score for student, score in scores.items() if score >= 80}
# # # for name, score in scores.items():
# # #     if score >= 80:
# # #         highscores[name] = score
# # print(highscores)
# # SET COMPREHENSION
# numbers = [1, 2, 2, 3, 3, 4, 5]
# squares = {number ** 2 for number in numbers}
# print(squares)

# pairs = ["EURUSD", "GBPUSD", "EURUSD", "AUDCAD", "GBPUSD"]
# lowercase_pair = {pair.lower() for pair in pairs}
# print(lowercase_pair)