import random


class Generator:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[0 for i in range(m)] for j in range(n)]

    def generate(self):
        for i in range(self.n):
            for j in range(self.m):
                self.matrix[i][j] = random.randint(-10, 10)

    def print(self):
        for i in range(self.n):
            for j in range(self.m):
                print(self.matrix[i][j], end=' ')
            print()
