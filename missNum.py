def missing(arr, n):

    expected = n * (n + 1) // 2

    actual = sum(arr)

    return expected - actual


arr = [1, 2, 4, 5]

print(missing(arr, 5))