import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = list(color)
        self.filled = True
        self.__sides = sides

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_color(self, r, g, b):
        return all(isinstance(val, int) and 0 <= val <= 255 for val in (r, g, b))

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __is_valid_sides(self, *new_sides):
        return (
            len(new_sides) == self.sides_count
            and all(isinstance(side, int) and side > 0 for side in new_sides)
        )

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius**2


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) == 1:
            # Если передано только одно значение, все рёбра должны быть одинаковыми
            self.set_sides(*([sides[0]] * 12))
        elif len(sides) != 12:
            # Если передано меньше или больше сторон, то устанавливаем рёбра как 1
            self.set_sides(*([1] * 12))

    def get_volume(self):
        edge = self.get_sides()[0]
        return edge**3


# Проверка
circle1 = Circle((200, 200, 100), 10)  # Цвет, стороны
cube1 = Cube((222, 35, 130), 6)

# Проверка изменения цветов
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())

cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка изменения сторон
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())

circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (длины окружности)
print(len(circle1))

# Проверка объёма куба
print(cube1.get_volume())