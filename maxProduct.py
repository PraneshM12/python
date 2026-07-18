def max_product(arr):

    arr.sort()

    return arr[-1], arr[-2]


print(max_product([1, 4, 3, 6, 7, 0]))