class PhoneNumber:
    def __init__(self, number):
        yy = list(number)
        zz = ""
        N = set([str(i) for i in range(2, 10)])
        X = set([str(i) for i in range(0, 10)])
        S = {'+', '(', ')', '-', '.', ' '}
        digit = 0
        for y in yy:
            if y in S:
                continue
            if digit > 9:
                raise ValueError("Too many digits")
            elif digit == 0:
                if y == "1":
                    continue
                if y in N:
                    zz += y
                    digit += 1
                    continue
            elif digit == 3:
                if y in N:
                    zz += y
                    digit += 1
                    continue
            else:
                if y in X:
                    zz += y
                    digit += 1
                    continue
            raise ValueError("Invalid number")
        if len(zz) < 10:
            raise ValueError("Too few digits")
        else:
            self.number = zz

        self.area_code = self.number[0:3]

    def pretty(self):
        return "(" + self.area_code + ")-" + self.number[3:6] + "-" + self.number[6:10]


