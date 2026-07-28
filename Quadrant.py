x = int(input())
y = int(input())

if x > 0 and y > 0:
    print("First Quadrant")
elif x < 0 and y > 0:
    print("Second Quadrant")
elif x < 0 and y < 0:
    print("Third Quadrant")
elif x > 0 and y < 0:
    print("Fourth Quadrant")
elif x == 0 and y == 0:
    print("Origin")
elif x == 0:
    print("Y-Axis")
else:
    print("X-Axis")