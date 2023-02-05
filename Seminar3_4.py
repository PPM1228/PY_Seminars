
# 4. Дан массив, состоящий из целых чисел. Напишите программу, 
# которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером)
# start_list = [3, 7, 1, 7, 1, 4, 9]
# -> 4


# start_list = [3, 7, 1, 7, 1, 4, 9]
# count = 0
# for start_list[] <= len(start_list):

# print(f'Кол-во элементов массива, больших предыдущего = {count}')




# start_list = [3, 7, 1, 7, 1, 4, 9]
# count = 0
# for i in range(1, len(start_list)):
#     if start_list[i - 1] < start_list[i]:
#         count += 1
# print(count)



# count = 0
# for i in range(len(start_list) - 1):
#     if start_list[i+1] > start_list[i]:
#         count += 1

# print(count)




   # Лекция 2:

list_1 = list()
list_1 = [1, 2, 3, 4]
# print(*list_1)
for i in list_1:
    print(i)
print(len(list_1))
print(list_1[1]) 

for i in range(5):
    list_1.append(i)
    print(list_1)
print(len(list_1))

print(list_1.pop(0))
print(list_1)

print(list_1.insert(0, 157))
print(list_1)
