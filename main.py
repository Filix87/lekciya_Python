# # Урок 2. Коллекции данных. Профилирование и отладка
# # Спиcки
# list_1 = []
# list_1 = list()
# list_1 = [1, 2, 3, 8]
# # print(*list_1)

# # перебирает значения в списке через цикл. Покажет каждый раз значение i
# for i in list_1:
#     print(i)

# # -----
# # Покажет размер списка
# print(len(list_1))

# # -----
# # Покажет элемент под введенным индексом
# print(list_1[-2])

# # -----
# # Добавляем в список новый элемент
# list_1 = [1, 5]
# print(list_1)
# list_1.append(8)
# print(list_1)
# list_1.append(85)
# print(list_1)

# # ----
# # Создаем пустой список и цикл для добавления нового элемента
# list_1 = []
# print(list_1)
# for i in range(5):
#     list_1.append(i)
#     print(list_1)

# # Удаление последнего значения
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop())  # 0
# print(list_1)  # [12, 7, -1, 21]
# print(list_1.pop())  # 21
# print(list_1)  # [12, 7, -1]
# print(list_1.pop())  # -1
# print(list_1)  # [12, 7]
# print(list_1.pop())  # 7
# print(list_1)  # [12]

# # Удаление конкретного элемента из списка
# list_1 = [12, 7, -1, 21, 0]
# print(list_1)
# print(list_1.pop(0))  # 12
# print(list_1)  # [7, -1, 21, 0]

# # Добавление элемента на нужную позицию
# list_1 = [12, 7, -1, 21, 0]
# print(list_1)
# print(list_1.insert(2, 11))
# print(list_1)  # [12, 7, 11, -1, 21, 0]

# # ------
# # Вывод данных из списка
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0])  # 1
# print(list_1[1])  # 2
# print(list_1[len(list_1) - 1])  # 10
# print(list_1[-5])  # 6
# print(list_1[:])  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2])  # [1, 2]
# print(list_1[len(list_1) - 2 :])  # [9, 10]
# print(list_1[2:9])  # [3, 4, 5, 6, 7, 8, 9]
# print(list_1[6:-18])  # []
# print(list_1[0 : len(list_1) : 6])  # [1, 7]
# print(list_1[::6])  # [1, 7]

# # ------
# # Кортежи
# t = ()
# print(type(t))

# t = (
#     1,
#     5,
#     3,
# )
# print(type(t))

# v = [1, 8, 9]
# print(v)
# print(type(v))

# v = tuple(v)
# print(v)
# print(type(v))

# a, b, c = v
# print(a, b, c)

# t = (
#     1,
#     2,
#     3,
#     5,
# )

# for i in range(len(t)):
#     print(t[i])

# # -------
# # Словари
# d = {}
# d = dict()

# d["q"] = "qwerty"
# print(d)

# d["w"] = "werty"
# print(d)

# # -----------

# colors = {"red", "green", "blue"}
# print(colors)  # {'green', 'blue', 'red'}
# colors.add("red")
# print(colors)  # {'green', 'blue', 'red'}
# colors.add("gray")
# print(colors)  # {'gray', 'green', 'blue', 'red'}
# colors.remove("red")
# print(colors)  # {'gray', 'green', 'blue'}
# colors.discard("red")  # ok
# print(colors)  # {'gray', 'green', 'blue'}
# colors.clear()  # { }
# print(colors)  # set()

# # -----------
