from mrjob.job import MRJob
from mrjob.step import MRStep
import os


f1 = open("./input/A512.txt", 'r+')
lines = f1.readlines()
n, _ = lines[0].split()

f2 = open("./input/B512.txt", 'r+')
lines = f2.readlines()
_, m = lines[0].split()

counter = 0

class MatrixMultiplication(MRJob):

    f = open('./output/output_matrix.txt', 'w')

    def mapper(self, _, line):
        global counter
        line = line.split()
        line = list(map(int, line))

        if len(line) == 3:
            row, col, value = line
        elif len(line) == 2 and counter == 1:
            row, value = line
            col = 0
        elif len(line) == 2 and counter == 0:
            counter = 1
            return

        filename = os.environ['mapreduce_map_input_file']

        if 'A' in filename:
            for i in range(0, int(m)):
                yield (row, i), (0, col, value)
        elif 'B' in filename:
            for j in range(0, int(n)):
                yield (j, col), (1, row, value)

    def reducer_multiply(self, keys, values):
        A = []
        B = []

        for value in values:
            if value[0] == 0:
                A.append(value)
            elif value[0] == 1:
                B.append(value)
        A = sorted(A, key=lambda x: x[1])
        B = sorted(B, key=lambda y: y[1])

        for _, colA, valA in A:
            for _, colB, valB in B:
                if colA == colB:
                    yield keys, valA * valB

    def reducer_sum(self, key, values):
        total = sum(values)
        yield key, total
        x, y = key[0], key[1]
        self.f.write(f"{x} {y} {total}\n")

    def steps(self): return [
        MRStep(mapper=self.mapper, reducer=self.reducer_multiply),
        MRStep(reducer=self.reducer_sum)
    ]

    def close(self):
        self.f.close()
