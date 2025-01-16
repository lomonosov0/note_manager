
username  = input("Введите имя пользователя: ")
title_0 = input("Введите заголовок заметки: ")
title_1st = input("Введите первый подзаголовок: ")
title_2st = input("Введите второй подзаголовок: ")
title_3st = input("Введите третий подзаголовок: ")

content = input("Описание заметки: ")
status = input("На каком этапе ваша заметка?: ")
created_date = str(input("Дата создания заметки: "))
issue_date = str(input("Дата истечения заметки: "))
title_all = [title_1st, title_2st, title_3st]

print(f"Имя: {username}\nЗаголовок: {title_0}")
print("(Подзаголовки): ")
for title in title_all:
    print(title)
print(f"Описание заметки: {content}\nСтатус: {status}\nДата создания: {created_date}\nДата истечения: {issue_date}\n")



