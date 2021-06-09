def score(x, y):
    def mag(a, b):
        return pow(pow(a, 2) + pow(b, 2), 0.5)
    if mag(x, y) > 10:
        return 0
    elif mag(x, y) > 5:
        return 1
    elif mag(x, y) > 1:
        return 5
    else:
        return 10
