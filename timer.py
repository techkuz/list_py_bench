"""
Homegrown timing tools for function calls.
Does total time, best-of time, and best-of-totals time
"""
import time, sys


timer = time.clock if sys.platform[:3] == 'win' else time.time


def total(reps, func, *args, **kwargs):
    """
    Total time to run func() reps times.
    Returns (total time, last result)
    """
    reps_list = list(range(reps))
    start = timer()
    for rep in reps_list:
        result = func(*args, **kwargs)
    elapsed = timer() - start
    return elapsed, result


def best_of(reps, func, *args, **kwargs):
    """
    Quickest func() among reps runs.
    Returns (best time, last result)
    """
    best = 2 ** 32
    for rep in range(reps):
        start = timer()
        ret = func(*args, **kwargs)
        elapsed = timer() - start
        if elapsed < best:
            best = elapsed
    return best, ret


def best_of_total(reps1, reps2, func, *args, **kwargs):
    """
    Best of totals:
    (best of reps1 runs of (total of reps2 runs of func))
    """
    return best_of(reps1, total, reps2, func, *args, **kwargs)
