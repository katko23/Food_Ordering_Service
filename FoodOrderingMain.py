import OrderSenderCheck, FoodOrderingServer, time
import MenuSender

if __name__ == "__main__":

    server = FoodOrderingServer.Server()
    server.start()

    orderSender = OrderSenderCheck.OSender()
    orderSender.start()


    while(True):
        # time.sleep(20)
        MenuSender.menus()

