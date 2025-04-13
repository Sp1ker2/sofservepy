def task_3_2_1():
    chislo_1 = str(input( " chislo: "))
    summa = 0
    for i in chislo_1:
        i = int(i)
        summa +=i
    print(summa)
def task_3_2_2():
    chislo_2 = list(input( " chislo: "))
    chislo_2.reverse()
    print(chislo_2)
def task_3_2_3():
    chislo_3 = list(map(int, input(" chislo: ")))
    for i in range(len(chislo_3)):
            for j in range(len(chislo_3)-1):
                if chislo_3[j]<chislo_3[j+1]:
                    chislo_3[j],chislo_3[j+1] = chislo_3[j+1], chislo_3[j]
    chislo_3.reverse()
    print(chislo_3)


