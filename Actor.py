import arcade
import random
from pyglet.window import mouse
roasting = 5.0


class Model:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
    def hit(self, other, hit_size):
        return (abs(self.x - other.x) <= hit_size) and (abs(self.y - other.y) <= hit_size)

class Collectable(arcade.Sprite):
    """ This class represents something the player collects. """
    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        # Flip this once the coing has been collected.
        self.changed = False

class Player(Model):

    def __init__(self, world, x,y):
        super().__init__(world, x, y)

    def on_mouse_motion(self,x, y, dx, dy):
        self.x = x
        self.y = y

    def update(self, delta):
       pass

class Pig(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        # Flip this once the coing has been collected.
        self.changed = False
    def update(self):
        pass
        
class Beef(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        # Flip this once the coing has been collected.
        self.changed = False
    def update(self):
        pass

class Chicken(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        # Flip this once the coing has been collected.
        self.changed = False
    def update(self):
        pass

class Stove1(Model):

    def __init__(self, world, x,y):
        super().__init__(world, x, y)

    def update(self, delta):
        pass
class Stove2(Model):

    def __init__(self, world, x,y):
        super().__init__(world, x, y)

    def update(self, delta):
        pass
class Stove3(Model):

    def __init__(self, world, x,y):
        super().__init__(world, x, y)

    def update(self, delta):
        pass
class Stove4(Model):

    def __init__(self, world, x,y):
        super().__init__(world, x, y)

    def update(self, delta):
        pass
class Stove5(Model):

    def __init__(self, world, x,y):
        super().__init__(world, x, y)

    def update(self, delta):
        pass
class Stove6(Model):

    def __init__(self, world, x,y):
        super().__init__(world, x, y)

    def update(self, delta):
        pass
class Stove7(Model):

    def __init__(self, world, x,y):
        super().__init__(world, x, y)

    def update(self, delta):
        pass
class Stove8(Model):

    def __init__(self, world, x,y):
        super().__init__(world, x, y)

    def update(self, delta):
        pass
class Stove9(Model):

    def __init__(self, world, x,y):
        super().__init__(world, x, y)

    def update(self, delta):
        pass
class Stove10(Model):

    def __init__(self, world, x,y):
        super().__init__(world, x, y)

    def update(self, delta):
        pass

class Button1(Model):

    def __init__(self, world, x,y):
        super().__init__(world, x, y)
        self.x = x
        self.y = y
    def update(self, delta):
        pass
class Button2(Model):

    def __init__(self, world, x,y):
        super().__init__(world, x, y)
        self.x = x
        self.y = y
    def update(self, delta):
        pass
class Button3(Model):

    def __init__(self, world, x,y):
        super().__init__(world, x, y)
        self.x = x
        self.y = y
    def update(self, delta):
        pass

class World:
    def __init__(self, width, height):
        
        #create player and set position.
        self.player = Player(self,500,500)
        #make the stove by a piece of stove(10piece)
        self.stove1 = Stove1(self,60,100) 
        self.stove2 = Stove2(self,100,100) 
        self.stove3 = Stove3(self,140,100) 
        self.stove4 = Stove4(self,183,100) 
        self.stove5 = Stove5(self,226,100) 
        self.stove6 = Stove6(self,266,100) 
        self.stove7 = Stove7(self,306,100) 
        self.stove8 = Stove8(self,343,100) 
        self.stove9 = Stove9(self,382,100) 
        self.stove10 = Stove10(self,423,100)
        #make buttons
        self.button1 = Button1(self,545,100)
        self.button2 = Button2(self,605,100)
        self.button3 = Button3(self,665,100)


    def update(self,delta):
        self.player.update(delta)
        self.stove1.update(delta)
        self.stove2.update(delta)
        self.stove3.update(delta)
        self.stove4.update(delta)
        self.stove5.update(delta)
        self.stove6.update(delta)
        self.stove7.update(delta)
        self.stove8.update(delta)
        self.stove9.update(delta)
        self.stove10.update(delta)
        self.button1.update(delta)
        self.button2.update(delta)
        self.button3.update(delta)


        if self.player.hit(self.stove1, 20):
            print("Touch stove1")
        if self.player.hit(self.stove2, 20):
            print("Touch stove2")
        if self.player.hit(self.stove3, 20):
            print("Touch stove3")




