class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Start drawing')

class Pen(Stationery):
    def draw(self):
        print(f'Draw by {self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'Draw by pencil {self.title}')

class Handle(Stationery):
    def draw(self):
        print(f'Draw by hand {self.title}')

pen = Pen("X")
pencil = Pencil('Y')
handle = Handle('Z')
for i in (pen, pencil, handle):
    i.draw()
