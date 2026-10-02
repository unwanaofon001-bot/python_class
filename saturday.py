# my_tuple = ("a", "b", "c")
# u,o, = my_tuple
# print(u)
# print(o)
store_list = [("mango", 8), 
              ("Orange", 9), 
              ("banana", 3)]

store_dict = {}

for key, value in store_list:
    store_dict[key] = value
print(store_dict) 