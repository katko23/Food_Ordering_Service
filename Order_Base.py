import threading

orders_lock = threading.Lock()
order_id = 0
orders = []
received_orders = []

def orders_pop(index):
    with orders_lock:
        return orders.pop(index)

def order_append(index, item):
    with orders_lock:
        orders.insert(index,item)

def order_registration(orders):
    import Menu_Base
    for o in orders:
        for r in Menu_Base.restaurants_registered:
            if o['restaurant_id'] == r['restaurant_id']:
                o['restaurant_address'] = r['address']
                o['order_id'] = order_id
                o["estimated_waiting_time"] = 0
