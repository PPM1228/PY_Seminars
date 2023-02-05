
# 3. Напишите программу для печати всех уникальных значений в словаре.
# {
#     1: 'Vlad',
#     2: 'Vlad',
#     3: 'Oleg'
# }
# -> 2


# my_dict = [{"1": "Vlad"}, {"2": "Vlad"}, {"3": "Oleg"}]
# for i in [1, 2, 3]:
#     my_dict [i]
# print((dict(my_dict)))


# houses = {}
# for i in [S1, S2, S3, S4, S5]:
#     houses[i['дом']] = houses.setdefault(i['дом'], 0) + 1
# print(houses)


my_dict = {
    "1": "Vlad", "2": "Vlad", "3": "Oleg"
    }
print(my_dict)
print(len(set(my_dict.values())))



# len_dict = len(d)

# list = []
# i = 1

# while i <= len_dict:
#     list.append(d.get(i))
#     i += 1

list_1 = d.values()

print(len(set(list_1)))