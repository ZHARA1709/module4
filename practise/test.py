from sorting_methods.pracrise4 import *

data_1 = list(map(int, input('Введите числа через пробел: ').split()))
data_2 = list(map(int, input('Введите числа через пробел: ').split()))
data_3 = list(map(int, input('Введите числа через пробел: ').split()))

bubble_sort(data_1)
selection_sort(data_2)
insertion_sort(data_3)

print('Сортировка пузырьком: ', data_1)
print('Сортировка выборкой: ', data_2)
print('Сортировка вставкой: ', data_3)