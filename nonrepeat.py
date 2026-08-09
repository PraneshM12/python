n = int(input("Enter number: "))

original = n
found = False

while n > 0:
    digit = n % 10
    temp = original
    count = 0

    while temp > 0:
        if temp % 10 == digit:
            count += 1
        temp //= 10

    if count == 1:
        print("First non-repeating digit:", digit)
        found = True
        break

    n //= 10

if not found:
    print("No non-repeating digit")