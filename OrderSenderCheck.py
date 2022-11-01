import time
from threading import Thread
import requests
import Setings
import Order_Base, Menu_Base


class OSender(Thread):

    host = Setings.hostName
    port = Setings.serverPort
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            if len(Order_Base.orders)>0:
                order_send = Order_Base.orders_pop(0)
                dictToSend = order_send.copy()
                dictToSend.pop("restaurant_id")
                for r in Menu_Base.restaurants_registered:
                    if order_send['restaurant_id'] == r['restaurant_id']:
                        address = r['address']
                res = requests.post("http://" + address + "/v" + str(order_send['restaurant_id']) + "/order", json=dictToSend)
                print('response from DinningHole:', res.text)
                dictFromServer = res.json()
                Order_Base.sended_orders.append(dictFromServer)
                # res = requests.post("http://" + str(self.host) + ":" + str(self.port) + "/v2/order",
                #                     json=dictFromServer)

            # if len(Menu_Base.restaurants)>0 and len(Order_Base.orders)>0:
            #     for r in Menu_Base.restaurants:
            #         Menu_Base.menu_append(r['menu'])
            #         # print(Menu_Base.restaurants)
            #         order_done = Order_Base.orders_pop(0)
            #         dictToSend = order_done
            #         dictToSend['priority'] = 4
            #         dictToSend['pick_up_time'] = time.time()
            #         Order_Base.order_append(0,order_done)
            #
            #         # print(str(r['address']) , "  " , dictToSend)
            #         res = requests.post("http://" + str(r['address']) + "/client", json=dictToSend)
            #         print('response from restaurant:', res.text)



