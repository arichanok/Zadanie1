print('Введите коэффиценты для уравнений: ')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
D=b ** 2 - 4 * a * c
print('Дискриминант уравнения равен:',D)
if D < 0:
    print('Дискриминант меньше нуля.')
    print('Корней нет.')
if D == 0:
    x = -b / (2 * a)
    print('Дискриминант равен нулю.')
    print('Уравнение имеет один корень:',x)
if D>0:
    x1=(-b-D**0.5)/(2*a)
    x2=(-b+D**0.5)/(2*a)
    print('Уравнение больше нуля.')
    print('Первый корень уравнения равен:',min(x1,x2))
    print('Второй корень уравнения равен:',max(x1,x2))
