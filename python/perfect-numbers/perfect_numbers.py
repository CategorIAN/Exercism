def classify(number):
    if number < 1:
        raise ValueError("should be a natural number")
    f = 0
    for i in range(1, number):
        if number % i == 0:
            f += i
    if f < number:
        return "deficient"
    elif f == number:
        return "perfect"
    else:
        return "abundant"
