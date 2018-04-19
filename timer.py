"""
Рассчитывает общее время, лучшее время и лучшее из общих время.
По мотивам Lutz, Mark. Learning Python: Powerful Object-Oriented Programming. " O'Reilly Media, Inc.", 2013.
"""
import time, sys

# проверка ОС для настройки времени
if sys.version_info[0] >= 3 and sys.version_info[1] >= 3:
    timer = time.perf_counter
else:
    timer = time.clock if sys.platform[:3] == 'win' else time.time


def total(reps, func, *args, **kwargs):
    """
    :param reps: количество повторений
    :param func: функция к тестированию
    :param args: позиционные аргументы
    :param kwargs: аргументы по ключам
    :return: общее время работы функции reps количество раз
    """
    reps_list = list(range(reps))
    start = timer()
    for rep in reps_list:
        func(*args, **kwargs)
    elapsed = timer() - start
    return elapsed


def best_of(reps, func, *args, **kwargs):
    """
    :param reps: количество повторений
    :param func: функция к тестированию
    :param args: позиционные аргументы
    :param kwargs: аргументы по ключам
    :return: самую быструю func среди reps количества запусков
    """
    best = 2 ** 32
    for rep in range(reps):
        start = timer()
        func(*args, **kwargs)
        elapsed = timer() - start
        if elapsed < best:
            best = elapsed
    return best


def best_of_total(reps1, reps2, func, *args, **kwargs):
    """
    :param reps1:
    :param reps2:
    :param func: функция к тестированию
    :param args: позиционные аргументы
    :param kwargs: аргументы по ключам
    :return: лучший результат из totals
    """
    return best_of(reps1, total, reps2, func, *args, **kwargs)
