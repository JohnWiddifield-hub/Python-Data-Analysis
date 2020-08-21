import numpy

if __name__ == "__main__":
    # a.) Generate a 10×10 identity matrix A.

    print("a.) Generate a 10×10 identity matrix A.")
    matrixA = numpy.identity(10)
    print(matrixA)

    # b.)Change all elements in the 7th column of A to 8
    print("\n" + "b.)Change all elements in the 7th column of A to 8")
    matrixA[:, 6] = 8
    print(matrixA)

    # c.)  Sum of all elements in the matrix (use a ”for/while loop”)
    print("\n" + "c.)  Sum of all elements in the matrix (use a ”for/while loop”)")
    sum = 0
    for arr in matrixA:
        for elem in arr:
            sum = sum + elem
    print(sum)

    # d.)Transpose the matrix A (A = AT).
    print("\n" + "d.)Transpose the matrix A (A = AT).")
    transposeMatrixA = matrixA.transpose()
    print(transposeMatrixA)

    # TODO:question on whether double count is ok, if it is asking for sum of each individual row or total sum
    # e.)Calculate sum of the 1st row, the diagonal and the 2nd column in the matrix A.
    print(
        "\n"
        + "e.) Calculate sum of the 1st row, the diagonal and the 2nd column in the matrix A."
    )
    sumDiagonal = numpy.sum(numpy.diag(matrixA))
    sumRow = numpy.sum(matrixA[0])
    sumCol = numpy.sum(matrixA[:, 1])
    print("Diagonal Sum: " + str(sumDiagonal))
    print("Row Sum: " + str(sumRow))
    print("Column Sum: " + str(sumCol))
    # f.)Generate a 10×10 matrix B following Gaussian Distribution with mean 12 and variance π.
    print(
        "\n"
        + "f.) Generate a 10×10 matrix B following Gaussian Distribution with mean 12 and variance π."
    )
    matrixB = numpy.random.normal(12, numpy.pi, size=(10, 10))
    print(matrixB)

    # g.) get matrix C
    print("\ng.) ")
    row1 = (matrixB[0] * matrixA[7]) - matrixB[:, 2]
    row2 = matrixA[3] - matrixB[:, 6]
    row3 = matrixA[:, 9] + matrixB[0]
    matrixC = numpy.array([row1, row2, row3])
    print(matrixC)

    # h.)

