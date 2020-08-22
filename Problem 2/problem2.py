import numpy

if __name__ == "__main__":
    # a.)Generate a 10×10 identity matrix A.
    print("a.) Generate a 10×10 identity matrix A.")
    matrixA = numpy.identity(10)
    print(matrixA)

    # b.)Change all elements in the 7th column of A to 8
    print("\n" + "b.)Change all elements in the 7th column of A to 8")
    matrixA[:, 6] = 8
    print(matrixA)

    # c.)Sum of all elements in the matrix (use a ”for/while loop
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

    # e.)Calculate sum of the 1st row, the diagonal and the 2nd column in the matrix A
    print(
        "\n"
        + "e.) Calculate sum of the 1st row, the diagonal and the 2nd column in the matrix A."
    )
    sumDiagonal = numpy.sum(numpy.diag(matrixA))
    sumRow = numpy.sum(matrixA[0])
    sumCol = numpy.sum(matrixA[:, 1])
    print("1st Row Sum: " + str(sumRow))
    print("Diagonal Sum: " + str(sumDiagonal))
    print("2nd Column Sum: " + str(sumCol))

    # f.)Generate a 10×10 matrix B following Gaussian Distribution with mean 12 and variance π.
    print(
        "\n"
        + "f.) Generate a 10×10 matrix B following Gaussian Distribution with mean 12 and variance π."
    )
    matrixB = numpy.random.normal(12, numpy.pi, size=(10, 10))
    print(matrixB)

    # g.)From A and B, use matrix operations to get a new 3×10 matrix C such
    #   that, the first row of C is equal to the 1st row of B times the 8th row of A minus
    #   the 3rd column of B, the second row of C is equal to the 4th row of A minus the 7th
    #   column of B, and the third row of C is equal to the sum of the 10th column of A
    #   and 1st row of B
    print(
        "\ng.) From A and B, use matrix operations to get a new 3×10 matrix C such"
        + "that, the first row of C is equal to the 1st row of B times the 8th row of A minus"
        + "the 3rd column of B, the second row of C is equal to the 4th row of A minus the 7th"
        + "column of B, and the third row of C is equal to the sum of the 10th column of A"
        + "and 1st row of B "
    )
    row1 = (matrixB[0] * matrixA[7]) - matrixB[:, 2]
    row2 = matrixA[3] - matrixB[:, 6]
    row3 = matrixA[:, 9] + matrixB[0]
    matrixC = numpy.array([row1, row2, row3])
    print(matrixC)

    # h.) From C, using one matrix operation to get a new matrix D such that,
    #   the first column of D is equal to the first column of C times 3, the second column
    #   of D is equal to the second column of C times 4 and so on.
    print(
        "\nh.) From C, using one matrix operation to get a new matrix D such that,"
        + "the first column of D is equal to the first column of C times 3, the second column"
        + "of D is equal to the second column of C times 4 and so on."
    )
    matrixD = []
    for i in range(0, len(matrixC)):
        count = 3
        matrixD.append(["", "", "", "", "", "", "", "", "", ""])
        for j in range(0, 10):
            matrixD[i][j] = matrixC[i][j] * count
            count = count + 1
    matrixD = numpy.array(matrixD)
    print(matrixD)

    # i.)Compute the covariance matrix of X, Y ,Z, M, N
    #    and P. Then compute the Pearson correlation coefficients between X and Y.
    print(
        "\ni.)Compute the covariance matrix of X, Y ,Z, M, N"
        + "and P. Then compute the Pearson correlation coefficients between X and Y."
    )

    X = numpy.array([2, 0, 2, 0])
    Y = numpy.array([9, 8, 4, 3])
    Z = numpy.array([7, 1, 7, 9])
    M = numpy.array([6, 4, 8, 2])
    N = numpy.array([5, 4, 9, 3])
    P = numpy.array([1, 5, 2, 4])
    testCovMatrix = numpy.cov([X, Y, Z, M, N, P])
    print(testCovMatrix)
    r = numpy.corrcoef(X, Y)
    print(r[0][1])

    # j.)Given the equation: mean(x^2) = (mean(x)^2+σ^2(x)) where x = [19, 12, 16, 6, 11, 27, 1, 29]^T. Please determine whether the equation holds when:
    #   i. σ(x) is the population standard deviation. Show your work.
    #   ii. σ(x) is the sample standard deviation. Show your work.
    print(
        "\nj.Given the equation: mean(x^2) = (mean(x)^2+σ^2(x)) x = [19, 12, 16, 6, 11, 27, 1, 29]^T. Please determine whether the equation holds when:"
    )
    print("i. σ(x) is the population standard deviation. Show your work.")
    x = numpy.array([19, 12, 16, 6, 11, 27, 1, 29])
    # gives x^2
    xSquare = numpy.multiply(x, x)
    # gives mean(x^2)
    xSquareMean = numpy.mean(xSquare)
    print("mean(x^2): " + str(xSquareMean))
    # gives mean(x)^2
    xMeanSquare = numpy.mean(x) ** 2
    print("mean(x)^2: " + str(xMeanSquare))
    # gives population standard deviation
    populationStd = numpy.std(x) ** 2
    print("Population Standard Deviation: " + str(populationStd))
    print("\nmean(x^2) = (mean(x)^2+populationσ^2(x))")
    print(
        str(xSquareMean) + " = (" + str(xMeanSquare) + " + " + str(populationStd) + ")"
    )
    popVal = xMeanSquare + populationStd
    print(str(xSquareMean) + " = " + str(popVal))
    print("The above equation holds for the population standard deviation")

    print("\nii. σ(x) is the sample standard deviation. Show your work.")
    print("mean(x^2): " + str(xSquareMean))
    print("mean(x)^2: " + str(xMeanSquare))
    # gives the sample standard deviation
    sampleStd = numpy.std(x, ddof=1) ** 2
    print("Sample Standard Deviation: " + str(sampleStd))
    print("\nmean(x^2) = (mean(x)^2+sampleσ^2(x))")
    sampleVal = xMeanSquare + sampleStd
    print(str(xSquareMean) + " = " + str(sampleVal))
    print("The above equation doesn't hold for the sample standard deviation")

