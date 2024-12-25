
username = "Дмитрий"
title = "Заметка"
content = "Важное"
status = "В работе"
created_date = "24. 12. 2024"
issue_date = "31. 12. 2024"

temp_issue_date = created_date[0:7]
temp_created_date = issue_date[0:7]

print("Имя пользователя:", username)
print("Заголовок заметки:", title)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", temp_issue_date)
print("Дата истечения заметки:", temp_created_date)
