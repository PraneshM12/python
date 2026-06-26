def find_missing(arr, n):

    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)

    return expected_sum - actual_sum


numbers = [1, 2, 3, 4, 5, 6, 8]

print("Missing Number:", find_missing(numbers, 6))