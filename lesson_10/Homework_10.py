# # Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:
# # сторона_а (довжина сторони a).
# # кут_а (кут між сторонами a і b).
# # кут_б (суміжний з кутом кут_а).
# # Необхідно реалізувати наступні вимоги:

# # Значення сторони сторона_а повинно бути більше 0.
# # Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
# # Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення кут_б обчислюється автоматично.

# Для встановлення значень атрибутів використовуйте метод __setattr__.

# a, alpha, beta
# a > 0
# alpha+beta = 180


from math import sin, radians

class Romb:
    def __init__(self, a, alpha):
        self.a = a
        self.alpha = alpha  # beta обчислюється автоматично

    def __setattr__(self, name, value):
        if name == "a":
            if value <= 0:
                raise ValueError("Сторона повинна бути більшою за 0")
            super().__setattr__(name, value)

        elif name == "alpha":
            if not (0 < value < 180):
                raise ValueError("Кут alpha має бути в межах від 0 до 180")
            super().__setattr__(name, value)
            # автоматично розраховуємо beta
            super().__setattr__("beta", 180 - value)

        elif name == "beta":
            raise AttributeError("beta встановлюється автоматично. Не можна задавати вручну.")
        else:
            super().__setattr__(name, value)

    def __str__(self):
        return f"Romb: a = {self.a}, alpha = {self.alpha}°, beta = {self.beta}°"

    def perimeter(self):
        return 4 * self.a

    def area(self):
        # Формула площі ромба: a² * sin(alpha)
        return (self.a ** 2) * sin(radians(self.alpha))

    def __add__(self, other):
        if isinstance(other, Romb):
            return self.area() + other.area()
        raise TypeError("Можна додавати лише об'єкти типу Romb")

# Демонстрація
r1 = Romb(10, 60)
r2 = Romb(20, 80)

print(r1)                 # Romb: a = 10, alpha = 60°, beta = 120°
print(r2)                 # Romb: a = 20, alpha = 80°, beta = 100°
print(r1 + r2)            # Сума площ
print(r1.perimeter())     # Периметр r1

