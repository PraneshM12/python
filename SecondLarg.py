n = int(input("Enter the number of elements: "))

largest = float('-inf')
second = float('-inf')

print("Enter the numbers:")

for i in range(n):
    num = int(input())

    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

if second == float('-inf'):
    print("There is no second largest number.")
else:
    print("Second Largest Number:", second)