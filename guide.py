my_dict = []
with open('guide.txt', 'r') as file:
   for i in file:
       my_list = i.split()
       my_dict.append({'Имя': my_list[0], 'Телефон':my_list[1], 'Комментарий': my_list[2]})

print(my_dict)
       
print(""" Выберите нужный пункт меню: \n\n
1. Показывать все контакты\n
2. Добавить контакт\n
3. Найти контакт\n
4. Изменить контакт\n
5. Удалить контакт\n
6. Выход из программы""")

while True:
    try:
        menu_item = int(input())
        break
    except ValueError:
        print("Вы ввели неверное значение. Выберите пункт из меню")
        next