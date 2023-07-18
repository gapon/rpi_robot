from pyPS4Controller.controller import Controller


class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_x_press(self):
       print("Hello world")

    def on_x_release(self):
       print("Goodbye world")

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.debug = False
controller.black_listed_buttons = [3,2,4,5,6, 7, 8,9,10,11, 12, 13,0,-1,-2,14,15, 1]
controller.listen(timeout=60)