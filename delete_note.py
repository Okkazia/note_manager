note1 = {"Имя": "Алексей",
         "Заголовок": "Список покупок",
         "Описание": "Купить продукты на неделю"}
note2 = {"Имя": "Мария",
         "Заголовок": "Учеба",
         "Описание": "Подготовиться к экзамену"}
note3 = {"Имя": "Иван",
         "Заголовок": "Отпуск",
         "Описание": "Купить билеты на самолет"}
  # Вносим списки с заметками в список
list_note = [note1, note2, note3]
  # Создаем функцию для вывода списка заметок
def print_list(notes):
    if not notes:
        print("Список заметок пуст")
        return
    print("Список заметок:")
    for index, note_ in enumerate(notes, 1):
        print("Заметка №", index)
        print("   Имя:", note_["Имя"])
        print("   Заголовок:", note_["Заголовок"])
        print("   Описание:", note_["Описание"])

print_list(list_note)
  # Основной цикл удаления заметок путем добавления их в список notes_to)del
while True:
    del_note = input(
        "\nВведите имя пользователя или заголовок заметки, которую хотите удалить:"
    ).strip()

    notes_to_del = []
    for i, note in enumerate(list_note):
        if (del_note.lower() == note["Имя"].lower()
                or del_note.lower() == note["Заголовок"].lower()):
            notes_to_del.append(i)
  # Удаляем заметки по индексу
    if notes_to_del:
        for i in sorted(notes_to_del, reverse=True):
            del list_note[i]
            print("Заметки, с указанным параметром, удалены")
    else:
        print("Такие заметки не найдены")
  # Предлагаем удалить еще заметки
    print_list(list_note)
    while True:
        ans = input("\nХотите удалить еще заметку? (Да/Нет):").strip().capitalize()
        if ans == "Да":
            break
        elif ans == "Нет":
            exit()
        else:
            print("Неправильный ввод. Попробуйте еще раз.")




