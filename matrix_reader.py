class Reader:
    def __init__(self, filename):
        self.filename = filename
        self.matrix = []
        self.n = 0
        self.m = 0

    def read(self):
        with open(self.filename, 'r+') as f:
            self.n, self.m = map(int, f.readline().split())
            self.matrix = [[0 for i in range(self.m)] for j in range(self.n)]
            for line in f:
                line = line.split()
                line = list(map(int, line))
                row, col, value = line
                self.matrix[row][col] = value

    def getMatrix(self):
        return self.matrix
