n = int(input())

while n != 1 and n != 4:
    total = 0

    while n > 0:
        digit = n % 10
        total += digit * digit
        n //= 10

    n = total

if n == 1:
    print("Happy Number")
else:
    print("Not Happy Number")