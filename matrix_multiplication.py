from mrjob.job import MRJob
from mrjob.step import MRStep
import sys
import os
import time

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
            yield col, (0, row, value)
        elif 'B' in filename:
            yield row,  (1, col, value)

    def reducer_multiply(self, keys, values):
        A=[]
        B=[]

        for value in values:
            if value[0] == 0:
                A.append(value)
            elif value[0] == 1:
                B.append(value) 

        for _, col0, val0 in A:
            for _, col1, val1 in B:
                yield (col0, col1), val0*val1

    def changeKey(self, key, value):
        yield key, value

    def reducer_sum(self, key, values):
        total = sum(values)
        yield key, total
        x, y = key[0], key[1]
        self.f.write(str(x) + " " + str(y) + " ")
        self.f.write(str(total) + "\n")

    def steps(self): return [
        MRStep(mapper=self.mapper, reducer=self.reducer_multiply),
        MRStep(mapper = self.changeKey, reducer=self.reducer_sum)
        ]
    
    def close(self):
        self.f.close()

if __name__ == '__main__':
    t0 = time.time()
    mm = MatrixMultiplication()
    mm.run()
    mm.close()
    t1 = time.time()

    time = t1 - t0
    print ("Total time for the multiplication: " + str(time))
