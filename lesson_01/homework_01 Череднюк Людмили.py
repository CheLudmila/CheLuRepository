# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
# варіант 1
apples = 2
bananas = apples * 4
print(f"Яблук: {apples}, Бананів: {bananas}")

# варіант 2
def calculate_bananas(apples):
    return apples * 4

# Отримуємо кількість яблук від користувача
apples = int(input("Введіть кількість яблук: "))
bananas = calculate_bananas(apples)

print(f"Яблук: {apples}, Бананів: {bananas}")


# task 05 == виправте назви змінних

storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача

storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

perimeter = storona_1 + storona_2 + storona_3 + storona_4

print("Периметр фігури:", perimeter)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""

# Скільки яблунь посадили
yabluni = 4

# Груш на 5 більше, ніж яблунь
grushi = yabluni + 5

# Слив на 2 менше, ніж яблунь
slyvy = yabluni - 2

# Загальна кількість дерев
vsego_derev = yabluni + grushi + slyvy

# Виводимо відповідь
print("Усього дерев у саду:", vsego_derev)

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
# Варіант 1
# температура до обіду
t_am = 5
# температура після обіду
t_pm = t_am - 10
# температура надвечір
t_evening = t_pm + 4

print("Температура надвечір:", t_evening)

# Варіант 2
# Температура до обіду
temperature_before_lunch = 5

# Температура після обіду опустилась на 10 градусів
temperature_after_lunch = temperature_before_lunch - 10

# Надвечір потепліло на 4 градуси
temperature_evening = temperature_after_lunch + 4

# Виводимо відповідь
print("Температура надвечір:", temperature_evening, "градусів")


# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
# Всього в театральному гуртку хлопчиків
boys = 24
# Всього в театральному гуртку дівчаток
girls = boys/2
# Кількість хворих хлопчиків
boys_ill = 1
# Кількість хворих дівчаток
girls_ill = 2
# Загальна кількість присутніх в гуртку
сount_all=boys+girls-boys_ill-girls_ill

print("Кількість присутніх сьогодні дітей в театральному гуртку:", int(сount_all))

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
# Вартість першої книжки
book1_price=8
# Вартість другої книжки
book2_price=book1_price+2
# Вартість третьої книжки
book3_price=(book1_price+book2_price)/2
# Вартість трьох книг, якщо купити по одному примірнику
all_price = book1_price+book2_price+book3_price


print("Всі книжки по 1 примірнику будуть коштувати:", (all_price), "грн")