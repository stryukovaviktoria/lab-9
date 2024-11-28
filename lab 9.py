import re

# Функція для пошуку дійсних чисел у тексті
def find_real_numbers(text):
    # Регулярний вираз для пошуку дійсних чисел
    pattern = r"-?\d+\.\d+|-?\d+"
    return re.findall(pattern, text)

# Читання вмісту файла TF14_1 та запис чисел у TF14_2
with open("TF14_1.txt", "r") as file:
    text = file.read()

# Знаходимо всі числа
numbers = find_real_numbers(text)

# Записуємо числа у файл TF14_2, розділяючи їх пробілами
with open("TF14_2.txt", "w") as file:
    file.write(" ".join(numbers))

import re

# Функція для пошуку дійсних чисел у тексті
def find_real_numbers(text):
    # Регулярний вираз для пошуку дійсних чисел
    pattern = r"-?\d+\.\d+|-?\d+"
    return re.findall(pattern, text)

# Читання вмісту файла TF14_1 та запис чисел у TF14_2
with open("TF14_1.txt", "r") as file:
    text = file.read()

# Знаходимо всі числа
numbers = find_real_numbers(text)

# Записуємо числа у файл TF14_2, розділяючи їх пробілами
with open("TF14_2.txt", "w") as file:
    file.write(" ".join(numbers))

# Читання чисел із файла TF14_2
with open("TF14_2.txt", "r") as file:
    numbers_text = file.read()

# Перетворення рядка з числами у список чисел
numbers = list(map(float, numbers_text.split()))

# Знаходимо найбільше число
max_number = max(numbers)

print(f"Найбільше число: {max_number}")
