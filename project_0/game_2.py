"""Игра угадай число
Компьютер сам число угадывает"""

import numpy as np

number = np.random.randint(1, 100)  # загадываем число


def random_predict(number: int = 1) -> int:
    count = 0
    while True:
        count += 1
        predict_numner = np.random.randint(1, 100)  # предполагаемое число
        if number == predict_numner:
            break  # выход из цикла
    return (count)  # число попыток


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 угадывает наш подход

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(
        1, 100, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Алгоритм угадывает число в среднем за {score} попыток")
    return score


if __name__ == '__main__':
    score_game(random_predict)
