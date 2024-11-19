my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
counter = 0

while counter < len(my_list):
    i = my_list[counter]
    if i == 0:
        counter += 1
        continue
    elif i < 0:
        break
    else:
        print(i)
    counter += 1