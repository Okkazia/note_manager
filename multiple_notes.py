
list_notes = []
def create_note(** values):
    global list_notes
    list_notes.append(values)

print("Добро пожаловать в 'Менеджер заметок'! Вы можете добавить новую заметку.")
while True:
    ans = input("Хотите добавить заметку?(Да/Нет):")
    if ans == "Да":
        create_note(
            username=input("Введите имя пользователя: "),
            title=input("Введите заголовок заметки: "),
            content=input("Введите описание заметки: "),
            status=input("Введите статус заметки: "),
            created_date=input("Введите дату создания заметки в формате: Число.Месяц.Год. "),
            issue_date=input("Введите дату истечения заметки в формате: Число.Месяц.Год. "))
        print("Заметка добавлена! Можно добавить еще.")
    elif ans == "Нет":
        break
    else:
        print("Некорректный ввод. Попробуйте еще раз.")


for i in list_notes:
    print("\n"'Заголовок заметки:', i["title"])
    print('Имя пользователя:', i["username"])
    print('Описание заметки:', i["content"])
    print('Статус заметки:', i["status"])
    print('Дата создания заметки:', i["created_date"])
    print('Дата истечения заметки:', i["issue_date"],)


