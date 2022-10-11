import threading

menu_lock = threading.Lock()
menu = []
received_menu = []
restaurants = []

def menu_append(temp):
    with menu_lock:
        menu.append(temp)

