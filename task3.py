# -*- coding: cp1251 -*-
N = int(input("������ ����� N (1 < N < 9): "))
if 1 < N < 9:
    for i in range(N, 0, -1):
        print("5 " * i)
    for i in range(1, N + 1):
        print("5 " * i)
else:
    print("����� N ������� ���� � ����� 1 < N < 9")