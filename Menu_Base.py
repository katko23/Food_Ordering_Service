import threading

menu_lock = threading.Lock()
menu = []
received_menu = []
restaurants = []
restaurants_registered = []

def menu_append(temp):
    with menu_lock:
        menu.append(temp)

def menu_pop(index):
    menu.pop(index)

