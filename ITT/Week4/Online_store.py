pro_available = set()
n = int(input("Enter the Number of Products available:"))
for i in range(n):
    product = input("Enter the Product available:")
    pro_available.add(product)
print("Quantity of products available:",n)
print("Products Available:",pro_available)

pro_sold = set()
m = int(input("Enter the Number of Products sold:"))
for i in range(m):
   product = input("Enter the Product sold:")
   pro_sold.add(product)
print("Quantity of products sold:",m)
print("Products Sold:",pro_sold)

