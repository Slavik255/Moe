# 2 Задание
a = [[col for col in range(7)] for row in range(7)]
for i in a:
    """Исходный двумерный массив"""
    print(i)
for row_index, row in enumerate(a):
    for col_index in range(row_index, len(row)):
        tmp = a[col_index][row_index]  # Установить временную переменную
        a[col_index][row_index] = row[col_index]
        a[row_index][col_index] = tmp
"""Перевернутый на 90 градусов двумерный массив"""
print(a)
# enumerate() добавляет счетчик к итерации и возвращает его
# len() возвращает количество элементов (длину) в объекте
# index_col — задает номер столбца который будет использоватся в качестве индекс
# range() - позволяет генерировать ряд чисел в рамках заданного диапазона
# row - для подсчета количества строк запроса
# Как перевернуть что бы шло построчно!
