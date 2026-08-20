from Order import Order
from Subscribers.Inventory import Inventory
from Subscribers.Analytics import Analytics
from Subscribers.Customer import Customer

order = Order(order_id=1, customer_id=101, status="PLACED")

customer_subscriber = Customer(customer_id=101, name="John Doe")
inventory_subscriber = Inventory(order_id=1)
analytics_subscriber = Analytics(order_id=1)

order.add_subscriber(customer_subscriber)
order.add_subscriber(inventory_subscriber)  
order.add_subscriber(analytics_subscriber)

order.change_status("SHIPPED")