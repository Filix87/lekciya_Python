"""первая лекция"""
"""
print(5, 8, 6)

a = 123
b = 1.23
c = None
print(a)
print(b)
print(c)

n = 'hjhjhjh'
print(n)
n1 = "hjkhjhjhj"
print(n1)
"""
"""
n = 'kkkj'
print(type(n))
"""

"""
n = 'kk\'kj'
print(n)
# чтобы вывести ковычки, нужно добавить перед ними знак \

n = 'kk"тоже так норм выведет"kj'
print(n)
# чтобы вывести ковычки, нужно добавить перед ними знак ""
"""
"""
a = 5
b = 5.89
c = 'hello'

print(a, ' - ', b, ' - ', c)
"""
"""
print(f"{a} - {b} -{c}")
"""
"""
print("{} - {} - {}".format(a, b, c))
"""
# print('введите первую строку')
# a = input()
# print("первая строка: ", a)

# print('введите введите первое число: ')
# a = input()
# b = input('Введите второе число: ')

# print(a, '+', b, '=', a+b)

# c = 5.89
# print(c)
# print(type(c))
# c = int(c)
# print(c)
# print(type(c))

# c = 5.89
# print(c)
# print(type(c))
# c = str(c)
# print(c + '89')
# print(type(c))

# c = 1
# print(c)
# print(type(c))
# c = bool(c)
# print(c)
# print(type(c))

# print('Введите введите первое число: ')
# a = int(input())
# b = int(input('Введите второе число: '))

# print(a, ' + ', b, ' = ', a + b)

# a = 5.89956
# b = 6.556551
# print(round(a*b, 3))
# """при ввывоlе останется только три знака после запятой"""

# iter = 2
# iter += 3  # iter = iter + 3
# iter -= 4  # iter = iter - 4
# iter *= 5  # iter = iter * 5
# iter /= 5  # iter = iter / 5
# iter //= 5  # iter = iter // 5
# iter %= 5  # iter = iter % 5
# iter **= 5  # iter = iter ** 5

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Ну привет, ', username + '.', ' Что хотел?')

# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0:  # если остаток при делении числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2:  # делить числа не может превышать введенное число, деленное на 2
#         print(n)
#         flag = False
#     i += 1

# r = range(100, 0, -20)
# for i in r:
#     print(i)

# a = 'qwerty'
# for i in a:
#     print(i) # каждая буква слова qwerty выведеться на новой строке

line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
    print(line)  # выведет 5 раз строку из 5 звездочек
