import threading

orders_lock = threading.Lock()
orders = []
received_orders = []

def orders_pop(index):
    with orders_lock:
        return orders.pop(index)

def order_append(index, item):
    with orders_lock:
        orders.insert(index,item)
