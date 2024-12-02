"""
@name tipCalculator 
@desc A function that calculates the total bill based on the basic tip expectation
@input Bill Total
@return The various based on the tip percentage.
"""

print("Welcome To The Tip Calculator")
bill = float(input("What was the total of the bill? $"))
tip20 = 0.20
tip15 = 0.15
tip18 = 0.18

# Calculate the total of the bill based on the tip percentage 
total20 = round(bill + bill * tip20, 2)

print(f"The total of the bill if you pay 20% tip is: {total20}")

total15 = round(bill + bill * tip15, 2)
print(f"The total of the bill if you pay 15% tip is: {total15}")

total18 = round(bill + bill * tip18, 2)
print(f"The total of the bill if you pay 18% tip is: {total18}")