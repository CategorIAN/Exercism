def is_armstrong_number(number):
    i = 0
    L = []
    n = number
    k = 0
    while n > 0:
        j = n % 10
        L.append(j)
        n = (n - j) // 10
        i += 1
    for l in L:
        k += pow(l, i)
    return number == k
