# По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного
# из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным
# или равносторонним.

# воспользуемся теоремой неравенства треугольников

l1 = int(input('Первый отрезок: '))
l2 = int(input('Второй отрезок: '))
l3 = int(input('Третий отрезок: '))

if (l1 > l2 + l3) | (l2 > l1 + l3) | (l3 > l1 + l2):
    print('Нельзя составить треугольник')
elif l1 == l2 == l3:
    print('Треугольник равносторонний')
elif (l1 == l2) | (l1 == l3) | (l2 == l3):
    print('Треугольник равнобедренный')
else:
    print('Треугольник разносторонний')
