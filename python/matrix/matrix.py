class Matrix:
    def __init__(self, matrix_string):
        M = []
        for i in matrix_string.split("\n"):
            r = []
            for j in i.split(" "):
                r.append(int(j))
            M.append(r)
        self.M = M

    def row(self, index):
        return self.M[index-1]

    def column(self, index):
        C = []
        for r in self.M:
            C.append(r[index-1])
        return C

