# Задача 1: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# number = int(input('Enter three digit number to find the sum of its digits: '))
# if (number > 999):
#     print(f'You have entered the number that contains more than 3 digits')
# else:
#     print(f'Your number is - {number}')

# sum = 0
# a = number // 100
# b = number // 10 % 10
# c = number % 10

# result = a + b + c
# print(f'The sum of all digits in the number is - {result}')



# Пробовал для себя, так как еще не сильно в таком разбираюсь :)
# sum = 0
# while number > 0:
#     a = number % 10
#     sum = sum + a
#     number = number // 10 
# print(f'The sum of all digits in the number is - {sum}')






# Задача 2: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал 
# каждый ребенок, если известно, что Петя и Сережа сделали 
# одинаковое количество журавликов, а Катя сделала в два раза 
# больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10


sum = int(input('Enter the total number of origami cranes: '))
print(f'Total number of origami cranes is - {sum}')

div_sum = int(sum / 3)

k = int(div_sum * 2)

p = int(k / 4)

s = int(k / 4)

print (f'Katya made {k} cranes. Petya - {p} and Serezha - {s}')





# Задача 3: Вы пользуетесь общественным транспортом? Вероятно, 
# вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. Т.е. 
# билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам
# требуется написать программу, которая проверяет счастливость билета.
#
# 385916 -> yes
# 123456 -> no


# ticket_number = int(input('Enter your ticket number to check whether it\'s a lucky one or not: '))
# if (ticket_number > 999999):
#     print(f'You have entered the number that contains more than 6 digits')
# else:
#     print(f'Your ticket number is - {ticket_number}')

# first_digits = int(ticket_number / 1000)
# digit1 = round(first_digits//100)
# digit2 = round((first_digits%100)//10)
# digit3 = round(first_digits%10)

# print(first_digits)

# print(f'The 1st digit is - {digit1}')
# print(f'The 2nd digit is - {digit2}')
# print(f'The 3rd digit is - {digit3}')

# check1 = int(digit1 + digit2 + digit3)
# print(f'Sum of the first three digits is - {check1}')

# last_digits = int(ticket_number % 1000)
# digit4 = round(last_digits//100)
# digit5 = round((last_digits%100)//10)
# digit6 = round(last_digits%10)

# print(f'The 4th digit is - {digit4}')
# print(f'The 5th digit is - {digit5}')
# print(f'The 6th digit is - {digit6}')

# check2 = int(digit4 + digit5 + digit6)
# print(f'Sum of the first three digits is - {check2}')

# if check1 == check2:
#     print('Your ticket is lucky! :)')
# else:
#     print('Sorry, but your ticket is an ordinary one')







# Задача 4: Требуется определить, можно ли от шоколадки размером n × m долек
# отломить k долек, если разрешается сделать один разлом по прямой между 
# дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no


# n = int(input('Введите длину шоколадки: '))
# m = int(input('Введите ширину шоколадки: '))
# k = int(input('Введите количество долек, которые необходимо получить, после разлома шоколадки: '))

# piece = (((n * m) - k) % 2)
# if  piece == 0:
#     print('Да, получится')
# else:
#     print('Нет, не получится')