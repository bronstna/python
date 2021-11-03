class Road:
    def __init__(self, lenght, widht):
        self._lenght = lenght
        self._widht = widht
    def get_weight(self, spec_grav, thick):
        return self._lenght * self._widht * spec_grav * thick / 1000

x = Road(5000, 20)
print(x.get_weight(25, 5))
