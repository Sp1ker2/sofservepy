def task_3_1_1():
    a_1 = str(input( " : "))
    stroka = a_1.split()
    for i in stroka:
        if i == "better" or i == "never" or i == "is":
            print(f"{i} = slovo")
    print(a_1)
def task_3_1_2():
    a_2 = str(input( " : ").upper())
    print(a_2)
def task_3_1_3():
    a_3 = str(input( " a_3: ").replace("i", "&"))
    print(a_3)