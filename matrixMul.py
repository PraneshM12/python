r1 = int(input("Rows of A: "))
c1 = int(input("Columns of A: "))
r2 = int(input("Rows of B: "))
c2 = int(input("Columns of B: "))

if c1 != r2:
    print("Matrix multiplication is not possible.")
else:
    print("Enter Matrix A:")
    A = [list(map(int, input().split())) for _ in range(r1)]

    print("Enter Matrix B:")
    B = [list(map(int, input().split())) for _ in range(r2)]

    result = [[0 for _ in range(c2)] for _ in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += A[i][k] * B[k][j]

    print("Result:")
    for row in result:
        print(*row)