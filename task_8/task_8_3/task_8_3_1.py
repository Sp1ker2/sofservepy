from geometry import rectangle_area, triangle_area, circle_area

figure = input("Which area do you want to calculate (rectangle / triangle / circle)? ").strip().lower()

if figure == "rectangle":
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    print("Rectangle area:", rectangle_area(a, b))

elif figure == "triangle":
    a = float(input("Enter base a: "))
    h = float(input("Enter height h: "))
    print("Triangle area:", triangle_area(a, h))

elif figure == "circle":
    r = float(input("Enter radius r: "))
    print("Circle area:", circle_area(r))

else:
    print("Unknown figure.")
