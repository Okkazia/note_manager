from datetime import date  # Импортируем модуль date из библиотеки datetime

current_date = date.today()  # Вносим в переменную текущую дату
print("Текущая дата:", current_date)  # Выводим текущую дату

while True:  # Создаем цикл со 100% выполнением
    try:  # Используем конструкцию tru-except
        deadline = input(
            "Введите дату дедлайна (в формате год-месяц-день):"
        )  # Запрос к пользователю с уточнением
        deadline_date = date.fromisoformat(deadline)  # Переводим str в date
    except ValueError:  # Ошибка перевода формата
        print(
            "Некорректный формат даты. Попробуйте еще раз."
              )  # Сообщение пользователю
    else:  # Ввод без ошибки
        break  # Окончание цикла

tdelta = deadline_date - current_date  # Разница между датами

if current_date > deadline_date:  # Условие дедлайна в прошлом
    print("Внимание! Дедлайн истек", abs(tdelta.days), "д. назад.")
elif current_date < deadline_date:  # Условие дедлайна в будущем
    print("До дедлайна осталось", abs(tdelta.days), "д.")
else:  # Условие дня дедлайна
    print("Дедлайн сегодня!")
