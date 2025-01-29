
from datetime import date

note = {
        'username': "Алексей",
        'title': "Список покупок",
        'content': "Купить продукты на неделю",
        'status': "новая",
        'created_date': date.today(),
        'issue_date': "2025-01-31"}
# Функция для печати заметки
def print_note(note):
    print("\n"'Заголовок заметки:', note["title"])
    print('Имя пользователя:', note["username"])
    print('Описание заметки:', note["content"])
    print('Статус заметки:', note["status"])
    print('Дата создания заметки:', note["created_date"])
    print('Дата истечения заметки:', note["issue_date"], )

print_note(note)
# Функция для обновления данных заметки
def update_note(note):
        while True:
            note_param = input(
                "Какие данные вы хотите обновить? "
                "(username, title, content, status, issue_date):")

            if note_param in note:
                note_new_param = input(f"Введите новое значение для {note_param}: ")
                note[note_param] = note_new_param
# Проверка формата даты
                if note_param == 'issue_date':
                    try:
                        deadline_date = date.fromisoformat(note['issue_date'])
                        note['issue_date'] = deadline_date
                    except ValueError:
                        print("Некорректный формат даты. Попробуйте еще раз.")

                        continue
                break
            else:
                print("Неверный параметр. Попробуйте еще раз.")

        return note

note_ = update_note(note)

print_note(note)
