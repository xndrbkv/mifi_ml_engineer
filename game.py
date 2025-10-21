"""Игра угадай число"""

import numpy as np

number = np.random.randint(1, 100)  # загадываем число

# Количество попыток
count = 0

while True:
    count += 1
    predict_number = int(input("Угадай число "))

    if predict_number > number:
        print("Число больше загаданного")

    elif predict_number < number:
        print("Число меньше загаданного")

    else:
        print(f"Угадали число {number}, попыток {count}")
        break
