from threading import Thread
import threading, time
from flask import Flask, request, jsonify

import Setings, Menu_Base, Order_Base

hostName = Setings.serverName
serverPort = Setings.this_serverPort

class Server(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        app = Flask(__name__)

        @app.route('/order', methods=['POST'])
        def my_order_endpoint():
            input_json = request.get_json(force=True)
            # force=True, above, is necessary if another developer
            # forgot to set the MIME type to 'application/json'
            print('data from client:', input_json)
            serverLock = threading.Lock()
            serverLock.acquire()
            Order_Base.orders_lock.acquire()
            Order_Base.received_orders.append(input_json)
            Order_Base.orders = Order_Base.orders + input_json['orders']
            Order_Base.order_id = Order_Base.order_id + 1
            # Order_Base.received_orders.append(1)
            Order_Base.orders_lock.release()
            serverLock.release()
            # time.sleep(100)
            # print("Append raw orders to the queue")
            while(len(Order_Base.sended_orders) < 2) : time.sleep(10)
            dictToReturn ={'orders_id':Order_Base.order_id,'orders':[Order_Base.sended_orders.pop(0), Order_Base.sended_orders.pop(0)]}
            return jsonify(dictToReturn)

        @app.route('/register', methods=['POST'])
        def my_register_endpoint():
            input_json = request.get_json(force=True)
            # force=True, above, is necessary if another developer
            # forgot to set the MIME type to 'application/json'
            print('data from Restaurant:', input_json)
            serverLock = threading.Lock()
            serverLock.acquire()
            Menu_Base.menu_lock.acquire()
            Menu_Base.restaurants.append(input_json)
            Menu_Base.restaurants_registered.append(input_json)
            # Order_Base.received_menu.append(1)
            Menu_Base.menu.append(input_json['menu'])
            Menu_Base.menu_lock.release()
            serverLock.release()
            print("Get all the menus")

            dictToReturn = {"Received": "FO Service received the menu from Restaurant"}
            return jsonify(dictToReturn)




        app.run(host=hostName, port=serverPort, debug=False)