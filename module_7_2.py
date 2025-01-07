def custom_write(file_name, strings):
    result = {}
    line_count = 1
    with open(file_name, "w", encoding="utf-8") as f:
        for line in strings:
            result[(line_count, f.tell())] = line
            f.write(f"{line}\n")
            line_count += 1
    return result




info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]


result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)