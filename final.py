
username = input("Введите имя пользователя: ")
title = input("Введите первый заголовок заметки: ")
title1 = input("Введите второй заголовок заметки: ")
title2 = input("Введите третий заголовок заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки: ")
created_date = input("Введите дату создания заметки в формате: Число.Месяц.Год. ")
issue_date = input("Введите дату истечения заметки в формате: Число.Месяц.Год. ")

title_list = [title, title1, title2]

temp_issue_date = created_date[0:5]
temp_created_date = issue_date[0:5]

note = [
    username,
    content,
    status,
    temp_created_date,
    temp_issue_date,
    title_list
]

print("Имя пользователя:", note[0])
print("Первый заголовок заметки:", note[5][0])
print("Второй заголовок заметки:", note[5][1])
print("Третий заголовок заметки:", note[5][2])
print("Описание заметки:", note[1])
print("Статус заметки:", note[2])
print("Дата создания заметки:", note[3])
print("Дата истечения заметки:", note[4])
