bill = float(input("Enter bill amount: "))

if bill > 5000:
    discount = bill * 0.20
elif bill > 1000:
    discount = bill * 0.10
else:
    discount = 0

final_amount = bill - discount

print("Discount:", discount)
print("Amount to Pay:", final_amount)