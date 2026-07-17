def kth_largest(arr, k):

    arr.sort(reverse=True)

    return arr[k - 1]


arr = [7, 10, 4, 3, 20, 15]

print(kth_largest(arr, 3))