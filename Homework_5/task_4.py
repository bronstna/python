class Car:
    def __init__(self, speed, colour, name, is_police=False):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = is_police

    def go(self):
        print('GO')
    def stop(self):
        print('STOP')
    def turn(self, direction):
        print(f'CAR TURNED TO {direction}')
    def show_speed(self):
        print(f'SPEED IS {self.speed}')

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('SPEED LIMIT')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('SPEED LIMIT')

class PoliceCar (Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

town = TownCar(70,'white', 'Town')
sport = SportCar(200, 'yellow', 'Sport')
work = WorkCar(50, 'red', 'Work')
police = PoliceCar(90, 'black', 'Police')

town.show_speed()
work.show_speed()

work.speed = 25
work.show_speed()

police.turn("Right")
