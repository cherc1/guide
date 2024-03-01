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
        
def show_all(my_dict):
    print("Выводим на экран телефонный справочник")
    print
    for i in my_dict:
        print(i)

show_all(my_dict)

def add_contact(my_dict):
    name = input("Введите имя: \n")
    phone = input("Введите телефон: \n")
    comment = input("Введите комментарий: \n")
    new_string = f'{name} {phone} {comment}'
    my_dict.append({'Имя': name, 'Телефон': phone, 'Комментарий': comment})
    with open('guide.txt', '+a') as file:
        file.write(new_string)

show_all(my_dict)
add_contact(my_dict)
show_all(my_dict)