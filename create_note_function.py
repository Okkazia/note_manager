
from datetime import date
# Функция для создания заметок с проверкой формата даты
def create_note():
    while True:
        try:
            note = {
                'username': input("Введите имя пользователя: "),
                'title': input("Введите заголовок заметки: "),
                'content': input("Введите описание заметки: "),
                'status': input("Введите статус заметки: "),
                'created_date': date.today(),
                'issue_date': input(
                    "Введите дату истечения заметки в формате: Год-Месяц-Число. ")}
            deadline_date = date.fromisoformat(note['issue_date'])
            note['issue_date'] = deadline_date
            break
        except ValueError:
            print("Некорректный формат даты. Попробуйте еще раз.")

    return note
# Создание заметки при помощи функции
note1 = create_note()
# Вывод заметки
print("\n"'Заголовок заметки:', note1["title"])
print('Имя пользователя:', note1["username"])
print('Описание заметки:', note1["content"])
print('Статус заметки:', note1["status"])
print('Дата создания заметки:', note1["created_date"])
print('Дата истечения заметки:', note1["issue_date"],)