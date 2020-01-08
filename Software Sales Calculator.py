# Let user enter the number of packages
quantity = int(input('Enter the number of packages ordered: '))
# For different quantities, the discount is different
if quantity >= 0 and quantity <= 9:
    discount = 0
elif quantity >= 10 and quantity <= 19:
    discount = 0.1
elif quantity >= 20 and quantity <= 49:
    discount = 0.2
elif quantity >= 50 and quantity <= 99:
    discount = 0.3
elif quantity >= 100:
    discount = 0.4
# Total cost is the cost before discount subtracted by the discounted cost
total_cost = round(quantity * 100 * (1 - discount),1)
total_discount = round(quantity * 100 - total_cost)
print('The total cost of your purchase was $', total_cost, 'with a discount of $', total_discount,'.')

