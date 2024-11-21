# -*- coding: cp1251 -*-
N = int(input("Введіть число N (1 < N < 9): "))
if 1 < N < 9:
    for i in range(N, 0, -1):
        print("5 " * i)
    for i in range(1, N + 1):
        print("5 " * i)
else:
    print("Число N повинно бути в межах 1 < N < 9")