def how_day_on_week(day):
    days = {
        1: 'Понедельник',
        2: 'Вторник',
        3: 'Среда',
        4: 'Четверг',
        5: 'Пятница',
        6: 'Суббота',
        7: 'Воскресенье'
    }
    return days[day]

try:
    day_on_week = int(input("Введите день недели (1-7): "))
    if day_on_week < 1 or day_on_week > 7:
        print("Ошибка: такого дня недели нет")
    else:
        print(how_day_on_week(day_on_week))
except ValueError:
    print("Ошибка: это не число")
