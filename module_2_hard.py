def generate_password(n):
    result = ""

    for i in range(1, n):
        for j in range(i + 1, 20):
            if n % (i + j) == 0 and (i + j) <= n:
                result += f"{i}{j}"

    return result


n = int(input("Введите число (от 3 до 20): "))
if 3 <= n <= 20:
    password = generate_password(n)
    print(f"Пароль для числа {n}: {password}")
else:
    print("Число должно быть в диапазоне от 3 до 20.")

