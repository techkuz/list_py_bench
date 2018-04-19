"""
Генерация листов различными способами
По мотивам Lutz, Mark. Learning Python: Powerful Object-Oriented Programming. " O'Reilly Media, Inc.", 2013.
"""

import timer


def for_loop():
    res = []
    for rep in reps_list:
        res.append(abs(rep))
    return res


def list_comprehension():
    return [abs(rep) for rep in reps_list]


def map_call():
    return list(map(abs, reps_list))


def gen_expr():
    return list(abs(rep) for rep in reps_list)


def gen_func():
    def gen():
        for rep in reps_list:
            yield abs(rep)
    return list(gen())


if __name__ == '__main__':
    reps = 10000
    reps_list = list(range(reps))

    for test_func in (for_loop, list_comprehension, map_call, gen_expr, gen_func):
        best_of = timer.best_of_total(5, 1000, test_func)
        print('%-9s: %.5f' % (test_func.__name__, best_of))
