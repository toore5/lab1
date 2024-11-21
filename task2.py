# -*- coding: cp1251 -*-
print('Програма обчислить суму парних чисел та добуток непарних чисел у діапазоні від 0 до 20.\n')
even_sum = 0
odd_product = 1
for i in range(21):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_product *= i
print('Сума парних чисел у діапазоні: ', even_sum, '\nДобуток непарних чисел у діапазоні: ', odd_product)
