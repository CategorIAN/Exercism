from copy import copy

def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    L = []
    R = copy(scores)
    for i in range(3):
        if not R:
            break
        x = max(R)
        L.append(x)
        R.remove(x)
    return L
