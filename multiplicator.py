import os
import time

from matrix_reader import Reader

def multiply(A, B):
    n = len(A)
    m = len(B[0])
    C = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    return C

A = []
B = []

ft = open("./times/classic_mult_times.txt", "w+")

for filename in os.listdir("./input"):
    if filename.startswith("A"):
        A.append(filename)
    elif filename.startswith("B"):
        B.append(filename)

for fa, fb in zip(sorted(A, key=len), sorted(B, key=len)):
    readerA = Reader("./input/" + fa)
    readerB = Reader("./input/" + fb)
    readerA.read()
    readerB.read()
    mtxA = readerA.getMatrix()
    mtxB = readerB.getMatrix()
    start = time.time()
    mtxC = multiply(mtxA, mtxB)
    end = time.time()
    print(f"Time elapsed for {fa} and {fb}: {end - start}")
    ft.write(f"{end - start}\n")

ft.close()
