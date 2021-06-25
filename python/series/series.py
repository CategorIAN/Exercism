def slices(series, length):
    L = len(series)
    ss = []
    if length > L or length < 1:
        raise ValueError("Invalid Length")
    else:
        for i in range(L-length+1):
            ss.append(series[i:i+length])
    return ss
