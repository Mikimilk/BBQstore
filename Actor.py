import arcade
from pyglet.window import key

class Model:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

class Player(Model):

    def __init__(self, world, x,y):
        super().__init__(world, x, y)

    def control(self, keys):

        if keys[key.LEFT]:
            self.x -= 10
        if keys[key.RIGHT]:
            self.x += 10
        if keys[key.UP]:
            self.y += 10
        if keys[key.DOWN]:
            self.y -= 10

    def update(self, delta):
        if self.x<0:
            self.x = 0
class Beef(Model):

    def __init__(self, world, x,y):
        super().__init__(world, x, y)

    def update(self, delta):
        if self.x<0:
            self.x = 0
class Pig(Model):

    def __init__(self, world, x,y):
        super().__init__(world, x, y)

    def update(self, delta):
        if self.x<0:
            self.x = 0
class Chic(Model):

    def __init__(self, world, x,y):
        super().__init__(world, x, y)

    def update(self, delta):
        if self.x<0:
            self.x = 0
class BeefWell(Model):

    def __init__(self, world, x,y):
        super().__init__(world, x, y)

    def update(self, delta):
        if self.x<0:
            self.x = 0
class PigWell(Model):

    def __init__(self, world, x,y):
        super().__init__(world, x, y)

    def update(self, delta):
        if self.x<0:
            self.x = 0
class ChicWell(Model):

    def __init__(self, world, x,y):
        super().__init__(world, x, y)

    def update(self, delta):
        if self.x<0:
            self.x = 0

class Tau(Model):

    def __init__(self, world, x,y):
        super().__init__(world, x, y)

    def update(self, delta):
        if self.x<0:
            self.x = 0
class Plate(Model):

    def __init__(self, world, x,y):
        super().__init__(world, x, y)

    def update(self, delta):
        if self.x<0:
            self.x = 0

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        self.player = Player(self,100,100)
        self.beef = Beef(self,500,100)
        self.pig = Pig(self,570,100)
        self.chic = Chic(self,640,100)
        self.tau = Tau(self,240,100)
        self.plate = Plate(self,240,240)
        self.beefW = BeefWell(self,65,240)
        self.pigW = PigWell(self,100,240)
        self.chicW = ChicWell(self,135,240)

    def control(self, keys):
        self.player.control(keys) 

    def update(self, delta):
        self.player.update(delta)
        self.beef.update(delta)
        self.pig.update(delta)
        self.chic.update(delta)
        self.tau.update(delta)
        self.plate.update(delta)
        self.beefW.update(delta)
        self.pigW.update(delta)
        self.chicW.update(delta)
