my_dict = []
with open('guide.txt', 'r') as file:
   for i in file:
       my_list = i.split()
       my_dict.append({'Имя': my_list[0], 'Телефон':my_list[1], 'Комментарий': my_list[2]})

print(my_dict)
       