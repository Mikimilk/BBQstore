import arcade
from pyglet.window import mouse

class Model:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
    def hit(self, other, hit_size):
        return (abs(self.x - other.x) <= hit_size) and (abs(self.y - other.y) <= hit_size)

class Player(Model):

    def __init__(self, world, x,y):
        super().__init__(world, x, y)

    def on_mouse_motion(self,x, y, dx, dy):
        self.x = x
        self.y = y


    def on_mouse_drag(self,x, y, dx, dy, buttons, modifiers):
        if buttons and mouse.LEFT:
            self.x = x
            self.y = y

    def update(self, delta):
        if self.x<0:
            self.x += 10
        elif self.x>self.world.width:
            self.x -=10
        elif self.y<0:
            self.y +=10
        elif self.y>self.world.height:
            self.y -=10


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


    def on_mouse_drag(self,x, y, dx, dy, buttons, modifiers):
        if self.player.hit(self.beef, 20):
            if buttons and mouse.LEFT:
                self.beef.x = x
                self.beef.y = y
        if self.player.hit(self.pig, 20):
            if buttons and mouse.LEFT:
                self.pig.x = x
                self.pig.y = y
        if self.player.hit(self.chic, 20):
            if buttons and mouse.LEFT:
                self.chic.x = x
                self.chic.y = y

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
        