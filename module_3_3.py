# Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(3, "test", False)
print_params(45, b="test1", c = True)

print_params(b = 25)
print_params(c = [1,2,3])


# Распаковка параметров:
values_list = ["Text", True, 25.5]
values_dict = {'a':"2", 'b':True, 'c': 453}

print_params(*values_list)
print_params(**values_dict)


# Распаковка + отдельные параметры:
values_list_2 = ['lorem', 2281]
print_params(*values_list_2, 42)
