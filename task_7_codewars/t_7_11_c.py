def count_sheeps(sheep):
    el = 0
    for i in sheep:
        if i == True:
            el += 1
    return el

print(count_sheeps([True, True, True, False,
                    True, True, True, True,
                    True, False, True, False,
                    True, False, False, True,
                    True, True, True, True,
                    False, False, True, True]))
