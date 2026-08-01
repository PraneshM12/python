r = int(input())
c = int(input())

A = [list(map(int, input().split())) for _ in range(r)]
B = [list(map(int, input().split())) for _ in range(r)]

for i in range(r):
    for j in range(c):
        print(A[i][j] + B[i][j], end=" ")
    print()