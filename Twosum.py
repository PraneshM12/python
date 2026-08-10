def two_sum(nums, target):
    seen = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in seen:
            return [seen[complement], i]

        seen[nums[i]] = i

    return []


# Input
nums = list(map(int, input("Enter the numbers: ").split()))
target = int(input("Enter the target: "))

# Function call
result = two_sum(nums, target)

# Output
if result:
    print("Indices:", result)
else:
    print("No two numbers found")