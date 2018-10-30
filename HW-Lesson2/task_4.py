# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.

# используем формулы для нахождения суммы n членов геометрической прогрессии
# http://www.grandars.ru/student/vysshaya-matematika/g-progressiya.html
b1 = 1
q = -0.5


def calculate_n_sum(n):
    n_member = b1 * (q ** (n - 1))
    return (1 - n_member * q) / (1 - q)


n = int(input('Введите кол-во членов геометрической прогрессии: '))

print(f'Сумма первых {n} членов геометрической прогрессии с q = {q} и b1 = {b1}: {calculate_n_sum(n)}')

# на всякий случай, если вдруг мы не можем использовать школьную математику ;)
# def calculate_n_sum(n):
#     result = 0
#     for i in range(n):
#         result += (-0.5) ** i
#     return result
#
# n = int(input('Введите кол-во членов геометрической прогрессии: '))
#
# print(f'Сумма первых {n} членов геометрической прогрессии 1 -0.5 0.25 -0.125...: {calculate_n_sum(n)}')