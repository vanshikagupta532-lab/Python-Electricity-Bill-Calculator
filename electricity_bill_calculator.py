print("===== Electricity Bill Calculator =====")

units = int(input("Enter electricity units consumed: "))

if units <= 100:
    bill = units * 5

elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)

else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

print("\nElectricity Units:", units)
print("Total Bill: ₹", bill)
if bill < 500:
    print("Category: Low Consumption")

elif bill < 1500:
    print("Category: Moderate Consumption")

else:
    print("Category: High Consumption")