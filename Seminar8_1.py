#Задача 49. Телефонный справочник

# Создать телефонный справочник с возможностью импорта и экспорта данных в 
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые 
# должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной 
# записи (Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

directory = open('phone_directory.txt', 'a')

def reading_output():
    with open('phone_directory.txt', 'r', encoding="utf-8") as directory:
        for line in directory:
            print(line)
    print(directory)

def adding(new_contact):
    with open('phone_directory.txt', 'a', encoding="utf-8") as directory:
        directory.write('\n' + new_contact)
    print(directory)


def searching(name):
    with open('phone_directory.txt', 'r', encoding="utf-8") as directory:
        for line in directory:
            if name in line:
                print(line)

def editing(contact_to_edit):
    directory = open('phone_directory.txt', 'r', encoding="utf-8")
    text = directory.read()
    directory.close()
    directory = open('phone_directory.txt', 'w', encoding="utf-8")
    text = input("Введите, данные для замены: ")
    directory.write(text.replace(contact_to_edit, text)) 
    directory.close()
    print('Done')
    

def remove_contact(contact_to_delete):
    with open('phone_directory.txt', 'r', encoding="utf-8") as directory:
        lines = directory.readlines()
        with open('phone_directory.txt', 'w', encoding="utf-8") as directory:
            for line in lines:
                if contact_to_delete in line:
                    print("Необходимые данные удалены")
                else:
                    print(line)    
                    directory.write(line)


def main_menu(number):
    if number == 1:
        reading_output()
    elif number == 2:
        data = input("Введите данные для добавления: ") 
        adding(data)
    elif number == 3:
        name = input("Введите имя для поиска: ")
        searching(name)
    elif number == 4:
        contact_to_edit = input("Введите контакт, который необходимо изменить: ")
        editing(contact_to_edit)
    elif number == 5:
        contact_to_delete = input("Введите данные для удаления: ")
        remove_contact(contact_to_delete)

while True:
    number = int(input("1 - для вывода всего справочника: "
                       "2 - для добавление новых данных: "
                       "3 - для поиска контакта: "
                       "4 - для внесения изменений: "
                       "5 - для удаления контакта: "
                       "6 - для выхода из меню: "))
    if number == 6:
        break
    main_menu(number)




    #Второе решение

# import os
# from data_create import name_data, surname_data, phone_data, adress_data

# file_name = "data.txt"
# def print_data():    
#     if os.path.exists(file_name):
#         print('Вывод данных из файла: ')
#         with open(file_name, 'r', encoding="utf-8") as file:
#             list_data = file.readlines()
#             for element in list_data:
#                 print(element)
#     else:
#         print("Файла не существует!!!")

# def input_data():
#     print('Введите данные для записи в файл: ')
#     name = name_data()
#     surname = surname_data()
#     phone = phone_data()
#     adress = adress_data()
#     with open(file_name, "a", encoding="utf-8") as file:
#         file.write(f"{name}; {surname}; {phone}; {adress};\n")

# def filter_data(filter_string):
#     with open(file_name, 'r', encoding="utf-8") as file:
#         list_data = file.readlines()
#         if ";" in filter_string:
#             list_filter = filter_string.split(";")
#         else:
#             list_filter = [filter_string]
#         is_found = False
#         for element in list_data:
#             temp_record = element.split("; ")
#             count = 0
#             for record in temp_record:                
#                 for element_filter in list_filter:
#                     if element_filter.lower() in record.lower() and len(element_filter.lower()) == len(record.lower()):
#                         count += 1

#             if count == len(list_filter):
#                 print(element)
#                 is_found = True
#     if not is_found:
#         print("Таких записей не нашли!")



#       Третье решение:

# print('1 - вывести все контакты \n ')
# print('2 - поиск контакта\n ')
# print('3 -добавить контакт\n ')
# print('4 - выход\n ')

# file_path = 'phone_book.txt'


# def tasks(task):
#     if task == 4:
#         print('до свидания')
#     else:
#         match task:
#             case 1:  # вывести все контакты
#                 with open(file_path, 'r', encoding='utf8') as open_book:
#                     for line in open_book:
#                         print(line)
# tasks(int(input('введите номер залачи от 1 до 4:')))
# case 2:  # поиск контактов
# with open(file_path, 'r', encoding='utf8') as open_book:
#     seach_param = input('Введите параметр для поиска: ')
#     for line in open_book:
#         if seach_param in line:
#             print(line)
# tasks(int(input('введите номер залачи от 1 до 4:')))

# case 3:  # добавить контакт
# with open(file_path, 'a', encoding='utf8') as open_book:
#     add_n1 = input('Введите фамилию: ')



# Соколов Иван Дмитриевич, 12345678
# Бережная Татьяна Валентиновна, 23456789
# Егорова Екатерина Алексеевна, 34567890
# Миягашев Филипп Филиппович, 45678901
# Боб Петров, 12345
# New contact


# Для себя:

    # with open('phone_directory.txt', 'r+', encoding="utf-8") as directory:
    #     contact_to_edit = directory.readlines()
    # new_data = input("Введите, данные для замены: ")
    # with open('phone_directory.txt', 'w', encoding='utf-8') as directory:
    #     directory.write(contact_to_edit.replace(contact_to_edit, new_data))
    #     directory.writelines(new_data)
    # print('Done')

# def editing(fileName, sourceText, replaceText):
#     file = open(fileName, 'r') #Opens the file in read-mode
#     text = file.read() #Reads the file and assigns the value to a variable
#     file.close() #Closes the file (read session)

#     file = open(fileName, 'w') #Opens the file again, this time in write-mode
#     file.write(text.replace(sourceText, replaceText)) #replaces all instances of our keyword
#     # and writes the whole output when done, wiping over the old contents of the file
#     file.close() #Closes the file (write session)
#     print 'All went well, the modifications are done'

    # def editing(contact_to_edit):
    # with open('phone_directory.txt', 'r+', encoding="utf-8") as directory:
    #     contact_to_edit = directory.readlines()
    #     new_data = input("Введите, данные для замены: ")
    #     new_data = new_data.replace(contact_to_edit, new_data)
    #     with open('phone_directory.txt', 'w+', encoding='utf-8') as directory:
    #         directory.writelines(new_data)


# def editing(contact_to_edit):
#     with open('phone_directory.txt', 'r+', encoding="utf-8") as directory, open('phone_directory1.txt', 'w', encoding="utf-8") as directory2:
#         new_data = input("Введите, данные для замены: ")
#         contact_to_edit = directory.readlines()
        # for line in contact_to_edit:
        #     line = line.strip()
        #     if line == new_data:
        #         directory2.writelines(contact_to_edit + '\n')
        #     else:
        #         directory2.writelines(line)
