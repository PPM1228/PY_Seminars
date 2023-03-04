# Задача 2
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке,
# причем кусты высажены только по окружности. Таким образом, у каждого куста есть 
# ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло 
# различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта 
# система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий 
# модуль за один заход, находясь непосредственно перед некоторым кустом, собирает 
# ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать 
# за один заход собирающий модуль, находясь перед некоторым кустом заданной во 
# входном файле грядки.
# 4
# 1 2 3 4
# 9


# garden = []
# n = int(input("Введите количество кустов: "))
# for berries in range(n):
#     berries = int(input("Введите количество ягод на кусте: "))
#     garden.append(berries)
# print(f"Кусты с ягодами: {garden}")

# max_berries = 0
# for berries in range(0, n):
#     if berries == n - 1:
#         berries_count = garden[berries] + garden[berries-1] + garden[0]
#         max_berries = max(berries_count, max_berries)
#     else:
#         berries_count = garden[berries] + garden[berries-1] + garden[berries+1]
#         max_berries = max(berries_count, max_berries)
# print(f"Максимальное количество ягод, которое может собрать сборщик - {max_berries}")


#   Второе решение

garden = []
n = int(input("Введите количество кустов: "))
for berries in range(n):
    berries = int(input("Введите количество ягод на кусте: "))
    garden.append(berries)
print(f"Кусты с ягодами: {garden}")


sum_garden = []
max_berries = garden[0] + garden[-1] + garden[-2]
temp_max_berries = 0
for i in range(0, n-1):
    berries_count = garden[i] + garden[i-1] + garden[i+1]
    temp_max_berries = berries_count
    if temp_max_berries > max_berries:
        max_berries = temp_max_berries
    sum_garden.append(max_berries)
print(max_berries)
