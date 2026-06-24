def second_largest(arr):

    largest = arr[0]
    second = arr[0]

    for num in arr:

        if num > largest:

            second = largest
            largest = num

        elif num > second and num != largest:

            second = num

    return second


numbers = [12, 45, 78, 23, 67]

print(second_largest(numbers))