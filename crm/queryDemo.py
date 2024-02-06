from accounts.models import *

# (1)Returns all customers from customer table
customers = Customer.objects.all()

# (2)Returns first customer in customer table
firstCustomer = Customer.objects.first()

# (3)Returns last customer in customer table
lastCustomer = Customer.objects.last()

# (4)Returns single customer by name
customerByName = Customer.objects.get(name='Lawrence Nderitu')

# (5)Returns single customer by Id
customerById = Customer.objects.get(id=3)

# (6)Returns all orders related to customer(first customer variable set above)
firstCustomer.order_set.all()

# (7)Returns orders customer name: (Query parent model values)
order = Order.objects.first()
parentName = order.customer.name

# (8)Returns products from products table with value of "Outdoor" in category attribute
products = Product.objects.filter(category="Outdoor")

# (9)Order/Sort Objects by Id
leastToGreatest = Product.objects.all().order_by('id')
greatestToLeast = Product.objects.all().order_by('-id')

# (10)Returns all products with tag of "Sports": (Query Many to Many Fields)
productsFiltered = Product.objects.filter(tags__name="Sports")

# (11)Bonus
