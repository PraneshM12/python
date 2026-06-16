nums = [2, 2, 1, 1, 2, 2, 2,3,4,3,4,6,3,3,3,4,2,32,]
candidate = None
count = 0

for num in nums:
    if count == 0:
        candidate = num

    count += 1 if num == candidate else -1

print(candidate)