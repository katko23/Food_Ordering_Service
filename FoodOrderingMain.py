import OrderSenderCheck, FoodOrderingServer

if __name__ == "__main__":

    server = FoodOrderingServer.Server()
    server.start()

    orderSender = OrderSenderCheck.OSender()
    orderSender.start()

