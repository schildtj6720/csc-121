# An assignment that makes use of decision structures and loops with the assignment on page 84 of the textbook.
# 2/9/2025
# CSC121 m2Lab– Function Review
# Jasmine Schildt

def eoq(demand, reorderCost, holdingCost, minOrder=0):
    eoq_total = (2 * demand * reorderCost / holdingCost) ** .5
    orderSize = max(eoq_total, minOrder) # account for the minimum order size
    return eoq_total, orderSize

# Prompt for and get inputs
demand = float(input("Enter the projected demand (units/year): "))
reorderCost = float(input("Enter the reorder cost ($/order): "))
holdingCost = float(input("Enter the holding cost ($/year/unit): "))
minOrder = float(input("Enter the minimum order size (units/order): "))

eoq_total, orderSize = eoq(demand, reorderCost, holdingCost, minOrder=0)

# Display results
print("\nEconomic Order Quantity:", round(eoq_total))
print("Order Quantity:", orderSize)
