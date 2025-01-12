
username = input("Введите имя пользователя: ")
title = input("Введите первый заголовок заметки: ")
title1 = input("Введите второй заголовок заметки: ")
title2 = input("Введите третий заголовок заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки: ")
created_date = input("Введите дату создания заметки в формате: Число. Месяц. Год. ")
issue_date = input("Введите дату истечения заметки в формате: Число. Месяц. Год. ")

title_list = [title, title1, title2]

temp_issue_date = created_date[0:7]
temp_created_date = issue_date[0:7]

print("Имя пользователя:", username)
print("Заголовки заметок:", title_list)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", temp_issue_date)
print("Дата истечения заметки", temp_created_date)