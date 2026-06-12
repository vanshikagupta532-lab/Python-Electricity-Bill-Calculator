print("===== ELECTRICITY BILL CALCULATOR =====")

customer_name = input("Enter Customer Name: ")
meter_number = input("Enter Meter Number: ")

units = int(input("Enter Units Consumed: "))

# Energy Charge Calculation
if units <= 100:
    energy_charge = units * 5

elif units <= 200:
    energy_charge = (100 * 5) + ((units - 100) * 7)

else:
    energy_charge = (100 * 5) + (100 * 7) + ((units - 200) * 10)

fixed_charge = 100

total_bill = energy_charge + fixed_charge

# Category
if units <= 100:
    category = "Low Consumption"
elif units <= 200:
    category = "Moderate Consumption"
else:
    category = "High Consumption"

print("\n===== BILL SUMMARY =====")
print("Customer Name :", customer_name)
print("Meter Number  :", meter_number)
print("Units Consumed:", units)
print("Energy Charge : ₹", energy_charge)
print("Fixed Charge  : ₹", fixed_charge)
print("Total Bill    : ₹", total_bill)
print("Category      :", category)
