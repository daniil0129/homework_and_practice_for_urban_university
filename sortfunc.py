num = [5, 6, 9, 3, 4]


def bubble_sort(ls):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i + 1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
                swapped = True
    return ls

print(bubble_sort(num))


def selection_sort(ls):
    for i in range(len(ls)):
        lowest = i
        for j in range(i, len(ls)):
            if ls[j] < ls[lowest]:
                lowest = j
        ls[i], ls[lowest] = ls[lowest], ls[i]


selection_sort(num)
print()