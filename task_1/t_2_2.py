
number = int(input("enter first number : "))
number_2 = int(input("enter second number : "))
znak = str(input(" enter + - / * // ** % "))
match znak:
    case "+":
        print(f"{number+number_2} ")
    case "*":
        print(f"{number * number_2}  ")
    case "-":
        print(f"{number - number_2}  ")
    case "/":
        print(f"{number / number_2} ")
    case "//":
        print(f"{number // number_2}  ")
    case "**":
        print(f"{number ** number_2}  ")
    case "%":
        print(f"{number % number_2} ")