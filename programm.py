class Progression:
    def __init__(self, n):
        self.a = 2
        self.d = 3
        self.n = n

    def n_element(self):
        an = self.a + self.d * (self.n - 1)
        if not isinstance(self.n, int):
            raise TypeError
        return an
pr = Progression(5)
print(pr.n_element())