
username = input("Введите имя пользователя: ")
title = input("Введите первый заголовок заметки: ")
title1 = input("Введите второй заголовок заметки: ")
title2 = input("Введите третий заголовок заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки: ")
created_date = input("Введите дату создания заметки в формате: Число.Месяц.Год. ")
issue_date = input("Введите дату истечения заметки в формате: Число.Месяц.Год. ")

title_list = [title, title1, title2]

temp_issue_date = created_date[0:6]
temp_created_date = issue_date[0:6]

note = [
    username,
    content,
    status,
    temp_created_date,
    temp_issue_date,
    title_list
]

print(note)