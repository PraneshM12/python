n = int(input())

temp = n
digit_sum = 0

while temp > 0:
    digit_sum += temp % 10
    temp //= 10

if n % digit_sum == 0:
    print("Harshad Number")
else:
    print("Not a Harshad Number")