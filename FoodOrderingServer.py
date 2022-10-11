from threading import Thread
import threading
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
            Order_Base.orders.append(input_json)
            # Order_Base.received_orders.append(1)
            Order_Base.orders_lock.release()
            serverLock.release()
            print("Append raw orders to the queue")
            dictToReturn = {'answer': "FO Service received the order"}
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
            # Order_Base.received_menu.append(1)
            Menu_Base.menu.append(input_json['menu'])
            Menu_Base.menu_lock.release()
            serverLock.release()
            print("Get all the menus")
            dictToReturn = {"Received": "FO Service received the menu from Restaurant"}
            return jsonify(dictToReturn)


        @app.route('/menu', methods=['Get'])
        def menu_endpoint():
            input_json = request.get_json(force=True)
            # force=True, above, is necessary if another developer
            # forgot to set the MIME type to 'application/json'
            print('data from client:', input_json)
            serverLock = threading.Lock()
            serverLock.acquire()

            serverLock.release()
            print("Send Menus to Client Service")
            dictToReturn = {'Answer': "FO Service received the menu from "}
            return jsonify(dictToReturn)

        app.run(host=hostName, port=serverPort, debug=False)