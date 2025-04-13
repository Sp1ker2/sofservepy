def task_3_3_1():
    a = int(input("chislo a : "))
    b = int(input("chislo b : "))
    print(a,b,"do pervorota")
    a,b = b,a
    print(a,b,"posle")