from matrix_generator import Generator
from matrix_writer import Writer


sizes = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
matrices = ["A", "B"]


if __name__ == '__main__':
    for size in sizes:
        for matrix in matrices:
            writer = Writer('./input/' + matrix + str(size) + '.txt')
            generator = Generator(size, size)
            generator.generate()
            mtx = generator.matrix
            writer.write(mtx)
            print("Generated matrix " + matrix + str(size) + ".txt")

    print("Done generating matrices")
