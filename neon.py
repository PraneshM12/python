n = int(input("Enter a number: "))

sq = n * n
s = 0

while sq:
    s += sq % 10
    sq //= 10

if s == n:
    print("Neon")
else:
    print("Not Neon")