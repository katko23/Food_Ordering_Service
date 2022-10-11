import time
from threading import Thread
import requests
import Order_Base,Menu_Base
import Setings


class OSender(Thread):

    host = Setings.hostName
    port = Setings.serverPort

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            if len(Order_Base.orders)>0:
                order_done = Order_Base.orders_pop(0)
                dictToSend = order_done
                time.sleep(2);
                res = requests.post("http://" + str(self.host) + ":" + str(self.port) + "/client", json=dictToSend)
                print('response from server:', res.text)
                dictFromServer = res.json()

            if len(Menu_Base.restaurants)>0:
                for r in Menu_Base.restaurants:
                    Menu_Base.menu_append(r['menu'])
                    # print(Menu_Base.restaurants)
                    order_done = Order_Base.orders_pop(0)
                    dictToSend = order_done
                    dictToSend['priority'] = 4
                    dictToSend['pick_up_time'] = time.time()
                    Order_Base.order_append(0,order_done)

                    # print(str(r['address']) , "  " , dictToSend)
                    res = requests.post("http://" + str(r['address']) + "/order", json=dictToSend)
                    print('response from restaurant:', res.text)



