from matrix_generator import Generator

class Writer:
    def __init__(self, filename):
        self.filename = filename

    def write(self, matrix):
        with open(self.filename, 'w+') as f:
            f.write(f"{len(matrix)} {len(matrix[0])}\n")
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] != 0:
                        f.write(f"{i} {j} {matrix[i][j]}\n")

    def getMatrix(self):
        return self.matrix
