def square_circle(x):
    square = 3.14 * x ** 2
    print("Площа круга:", square)

def square_triangle(x):
    square = 1/2 * x * (x + 1)
    print("Площа трикутника:", square)

def square_rectangle(x, y):
    square = x * y
    print("Площа прямокутника:", square)

who = input("Введи фігуру (circle, triangle, rectangle): ")

if who == "circle":
    square_circle(float(input("Радіус (y): ")))
elif who == "triangle":
    square_triangle(float(input("Сторона (x): ")))
elif who == "rectangle":
    square_rectangle(float(input("Сторона x: ")), float(input("Сторона y: ")))
else:
    print("Error: Невідома фігура")
