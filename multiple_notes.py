
from datetime import date

list_notes = []  # Создаем список для хранения словарей-заметок

def create_note(** values):  # Создаем функцию, добавляющую словари в список
    list_notes.append(values)

print("Добро пожаловать в 'Менеджер заметок'! Вы можете добавить новую заметку.")

while True:
    ans = (input(  # Запрашиваем ввод от пользователя и корректируем его
        "Хотите добавить заметку?(Да/Нет):").
           strip().capitalize())
    if ans == "Да":
        note = {  # Создание новой заметки
            'username': input("Введите имя пользователя: "),
            'title': input("Введите заголовок заметки: "),
            'content': input("Введите описание заметки: "),
            'status': input("Введите статус заметки: "),
            'created_date': input("Введите дату создания заметки в формате: Год-Месяц-Число. "),
            'issue_date': input("Введите дату истечения заметки в формате: Год-Месяц-Число. ")}
        try:  # Проверяем формат ввода даты
            created_date_ = date.fromisoformat(note['created_date'])
            deadline_date = date.fromisoformat(note['issue_date'])
            note['created_date'] = created_date_
            note['issue_date'] = deadline_date
        except ValueError:
            print("Некорректный формат даты. Попробуйте еще раз.")
            continue

        create_note(**note)  # Вызываем функцию и добавляем заметку в список
        print("Заметка добавлена! Можно добавить еще.")
    elif ans == "Нет":  # Оканчиваем добавление заметок
        break
    else:  # Исправляем пользователя
        print("Некорректный ввод. Попробуйте еще раз.")


for i in list_notes: # Вывод всех заметок
    print("\n"'Заголовок заметки:', i["title"])
    print('Имя пользователя:', i["username"])
    print('Описание заметки:', i["content"])
    print('Статус заметки:', i["status"])
    print('Дата создания заметки:', i["created_date"])
    print('Дата истечения заметки:', i["issue_date"],)
