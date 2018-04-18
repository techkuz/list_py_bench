"Test the relative speed of iteration tool alternatives."

import sys, timer


reps = 10000
reps_list = list(range(reps))


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


print(sys.version)
for test in (for_loop, list_comprehension, map_call, gen_expr, gen_func):
    (best_of, (total, result)) = timer.best_of_total(5, 1000, test)
    print('%-9s: %.5f => [%s...%s]' % (test.__name__, best_of, result[0], result[-1]))
    