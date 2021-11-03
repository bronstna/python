from time import sleep

class trafficlight:
    colors = ('red',  'yellow', 'green')
    delay = (7, 2, 8)

    def __init__(self):
        self.__color = 'green'

    def running(self):
        while True:
            for x in self.colors:
                self.__color = x
                print(self.__color)
                sleep(self.delay[self.colors.index(self.__color)])

traffic_light = trafficlight()
traffic_light.running()


