# -*- coding: cp1251 -*-
print('�������� ��������� ���� ������ ����� �� ������� �������� ����� � ������� �� 0 �� 20.\n')
even_sum = 0
odd_product = 1
for i in range(21):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_product *= i
print('���� ������ ����� � �������: ', even_sum, '\n������� �������� ����� � �������: ', odd_product)
