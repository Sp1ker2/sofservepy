"""Напишите функцию persistence, которая принимает положительный параметр
 num и возвращает его мультипликативную устойчивость, которая представляет 
 собой количество раз, которое необходимо умножить цифры в num, пока не получится одна цифра.
 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit, there are 3 multiplications)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2, there are 4 multiplications)
4 --> 0 (because 4 is already a one-digit number, there is no multiplication)
"""


# arr = list(map(str, input(": ").split()))
# print(arr)
# arr = input("; ")
# result = 1
#     for i in arr:
#     print(i)
#     dh = int(i)
#     result *= dh
# print(result)

# my_func = lambda x: if x>5 else x**2*my_func(10)
def my_func(x,y,z):
    print(x,y,z)
my_tuple = (1,2,3)
my_func(*my_tuple)