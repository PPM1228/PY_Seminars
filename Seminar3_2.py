# 2. Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K
# элементов вправо, K – положительное число.
# start_list = [1, 2, 3, 4, 5]
# k = 3
# -> [3, 4, 5, 1, 2]

start_list = [1, 2, 3, 4, 5]
k = int(input('Enter your number: '))

for 




    # Второй вариант решения


# staert_list = [1, 2, 3, 4, 5]
# num=50
# k = num%len(staert_list)
# staert_list_temp = [0]*len(staert_list)

# for i in range(len(staert_list)):
#     if (i+k)>= len(staert_list): 
#         staert_list_temp[i+k -len(staert_list)]= staert_list[i]
#     else: 
#         staert_list_temp[i+k] = staert_list[i]
# print(staert_list_temp)



    # Третий вариант решения



# start_list = [1, 2, 3, 4, 5]
# k = 7
# end_list=start_list.copy()
# # print(len(end_list))
# for i in range(len(start_list)):
#     if (i+k)<len(start_list):
#         end_list[i+k]=start_list[i]
#     else:
#         end_list[i+k%len(start_list)-len(start_list)]=start_list[i]
# print(end_list)





# k = 2
# start_list = [1, 2, 3, 4]
# new_list = []

# k = -(k%len(start_list))
# for i in start_list:
#     new_list.append(start_list[k])
#     k += 1
    
# print(new_list)

