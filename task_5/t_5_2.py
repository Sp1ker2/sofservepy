def fibonachi(dlina):
    if dlina <= 0:
        print([])
        return

    fib = [0, 1]
    while len(fib) < dlina:
        ch = fib[-1] + fib[-2]
        fib.append(ch)
    print(fib[:dlina])
fibonachi(9)