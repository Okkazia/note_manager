
username = input("Введите имя пользователя: ")
title = input("Введите заголовок заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки: ")
created_date = input("Введите дату создания заметки в формате: Число.Месяц.Год. ")
issue_date = input("Введите дату истечения заметки в формате: Число.Месяц.Год. ")

temp_issue_date = created_date[0:6]
temp_created_date = issue_date[0:6]

print("Имя пользователя:", username)
print("Заголовок заметки:", title)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", temp_issue_date)
print("Дата истечения заметки:", temp_created_date)
