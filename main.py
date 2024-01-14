import time
import sys

from matrix_multiplication2 import MatrixMultiplication


if __name__ == '__main__':
    ft = open("./times/mapreduce_mult_times.txt", "a+")
    start = time.time()
    mm = MatrixMultiplication()
    mm.run()
    mm.close()
    end = time.time()
    times = end - start
    print("Total time for multiplication: " + str(times))
    ft.write(str(times) + "\n")
    ft.close()
