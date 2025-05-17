def how_age(age):
    if age <= 0:
        raise ValueError("Возраст должен быть положительным числом")
    if age % 2 == 0:
        print("Возраст чётный")
    else:
        print("Возраст нечётный")

try:
    user_input = input("Введите ваш возраст: ")
    age = int(user_input) 
    how_age(age)
except ValueError as e:
    print("Ошибка:", e)
