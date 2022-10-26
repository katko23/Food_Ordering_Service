import Setings
import time
from threading import Thread
import requests

def menus():
    host = Setings.hostName
    port = Setings.serverPort
    import Menu_Base
    if(len(Menu_Base.restaurants) > 0):
        time.sleep(20);
        restaurants_data = []
        for r in Menu_Base.restaurants:
            temp = r.copy();
            del temp["address"];
            restaurants_data.append(temp)
        dictToSend = {"restaurants": len(Menu_Base.restaurants), "restaurants_data": restaurants_data}
        res = requests.get("http://" + str(host) + ":" + str(port) + "/menu", json=dictToSend)
        print('response from server:', res.text)
        Menu_Base.restaurants.clear()
        Menu_Base.menu.clear()

