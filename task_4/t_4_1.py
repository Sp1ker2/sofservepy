def task_4_1_1():
    C = int(input("temperature : "))
    F = (C*9/5)+32
    if F <-273.15:
        print(f"  {F} F Error: Temperature below absolute zero (-273.15°C)")
    else:
        print(f"your {F} F")
task_4_1_1()