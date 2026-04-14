#Генератор случайных чисел в заданном диапазоне. Не используйте готовые реализации ГПСЧ. 
# Отфильтруйте вывод генератора, чтобы он не содержал чисел с числом делителей больше n.

import time
from functools import reduce

# 1. Самодельный генератор случайных чисел (линейный конгруэнтный метод)
def my_random(min_val, max_val):
    # Используем время для начального зерна (seed)
    seed = int(time.time() * 1000) % 10000
    while True:
        # Формула ГПСЧ: X_next = (a * X + c) mod m
        seed = (1103515245 * seed + 12345) % 2**31
        # Приводим к нужному диапазону
        yield min_val + (seed % (max_val - min_val + 1))

# 2. Функция подсчета количества делителей через reduce
def count_divisors(num):
    if num == 0:
        return 0
    num = abs(num)
    # reduce собирает сумму единиц для каждого найденного делителя
    return reduce(
        lambda acc, i: acc + (1 if num % i == 0 else 0),
        range(1, int(num**0.5) + 1),
        0
    ) * 2 - (1 if int(num**0.5)**2 == num else 0)  # Корректировка для точных квадратов

# 3. Настройки
n = 4          # Максимально допустимое количество делителей
low, high = 1, 50  # Диапазон случайных чисел

# 4. Создаем генератор и фильтруем его
rand_gen = my_random(low, high)

# map применяет count_divisors к каждому числу
# filter пропускает только те, где делителей <= n
filtered_numbers = filter(
    lambda x: count_divisors(x) <= n,
    map(lambda _: next(rand_gen), range(20))  # Генерируем 20 чисел
)

# 5. Вывод результата
print(f"Числа из диапазона [{low}, {high}] с делителями ≤ {n}:")
for num in filtered_numbers:
    divs = count_divisors(num)
    print(f"{num} (делителей: {divs})")