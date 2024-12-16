import os

import math.sin, datetime.datetime

area = [["*", "*", "*"],
        ["*", "*", "*"],
        ["*", "*", "*"]]

def draw_area():
    for i in area:
        print('  '.join(i))

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Добро пожаловать в крестики нолики!")
    print("-----------------------------------")


print("Добро пожаловать в крестики нолики!")
print("-----------------------------------")
draw_area()
for turn in range(1, 10):
    if turn != 1:
        clear_console()
    print(f"Ход: {turn}")
    if turn % 2 == 0:
        turn_char = "0"
        print("Ходят нолики")
    else:
        turn_char = "X"
        print("Ходят крестики")
    row = int(input("Введите номер строки от 1 до 3: ")) - 1
    col = int(input("Введите номер столбца от 1 до 3: ")) - 1
    area[row][col] = turn_char
    draw_area()
