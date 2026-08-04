units = int(input("Enter units consumed: "))

bill = 0

if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = (100 * 1.5) + ((units - 100) * 2.5)
elif units <= 500:
    bill = (100 * 1.5) + (100 * 2.5) + ((units - 200) * 4)
else:
    bill = (100 * 1.5) + (100 * 2.5) + (300 * 4) + ((units - 500) * 6)

print("Energy Charge :", bill)

bill += 100
print("Meter Charge  :", 100)

if bill > 2000:
    surcharge = bill * 0.05
else:
    surcharge = 0

print("Surcharge     :", surcharge)
print("Final Bill    :", bill + surcharge)