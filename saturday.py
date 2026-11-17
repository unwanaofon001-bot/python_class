# # my_tuple = ("a", "b", "c")
# # u,o, = my_tuple
# # print(u)
# # print(o)
# store_list = [("mango", 8), 
#               ("Orange", 9), 
#               ("banana", 3)]

# store_dict = {}

# for key, value in store_list:
#     store_dict[key] = value
# print(store_dict)
# def category_totals(expenses):

#     store_cat = {}
    
   

#     for i in expenses:
#         amount = i["amount"]
#         category = i["category"]
    
#         if category in store_cat:
#             store_cat[category] += amount
#         else:    
#             store_cat[category] = amount
#     return store_cat
        


# if __name__ == "__main__":
#     print(category_totals([{"amount": 100, "category": "Food"}, {"amount": 100, "category": "Food"}, {"amount": 100, "category": "house"},
# {"amount": 100, "category": "house"}]))
#     print(category_totals([{"amount": 100, "category": "Food"}]))
#     print(category_totals([{"amount": 100, "category": "Food"}]))
#     print(category_totals([{"amount": 100, "category": "house"}]))
#     print(category_totals([{"amount": 100, "category": "house"}]))





# def count_correct(questions, answers):
#     total =0

#     for i in range (len(questions)):
#         if questions[i]["answer"] == answers[i]:
#             total += 1
#     return total        

# if __name__ == "__main__":
#     print(count_correct([{"answer": "a"}, {"answer": "b"}, {"answer": "a"}], ["a", "x", "a"]))    


def max_transaction(transactions):


if __name__ == " __main__":
    print(max_transaction([("deposit", 200), ("withdrawal", 100), ("deposit", 1000), ("withdrawal", 400)]))
