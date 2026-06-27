def longest_increasing_subarray(arr):

    start = 0
    max_start = 0
    max_len = 1

    for i in range(1, len(arr)):

        if arr[i] > arr[i - 1]:
            if i - start + 1 > max_len:
                max_len = i - start + 1
                max_start = start
        else:
            start = i

    return arr[max_start:max_start + max_len]


arr = [2, 5, 7, 3, 4, 6, 8, 1]

print(longest_increasing_subarray(arr)) 