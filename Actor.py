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
        self.mouse_drag = False
    
    #def on_mouse_drag(self,x, y, dx, dy, buttons, modifiers):
        #if buttons & mouse.LEFT:
            #self.mouse_drag = True
        
    def update(self, delta):
        pass
        
class Beef:
    def __init__(self):
        super().__init__()
        # Flip this once the coing has been collected.
        self.changed = False
        self.roasting_time = roasting
    def update(self,delta):
        self.roasting_time -= delta

class Pig:
    def __init__(self):
        super().__init__()
        # Flip this once the coing has been collected.
        self.changed = False
        self.roasting_time = roasting
    def update(self,delta):
        self.roasting_time -= delta

class Chicken:
    def __init__(self):
        super().__init__()
        # Flip this once the coing has been collected.
        self.changed = False
        self.roasting_time = roasting
    def update(self,delta):
        self.roasting_time -= delta

class Bag(Model): 
    def __init__(self, world ,x ,y):
        super().__init__(world ,x ,y)
        self.x = x
        self.y = y
    def update(self,delta):
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
        #make Beef class
        self.Beef_list = []
        beef = Beef()
        self.Beef_list.append(beef)
        #make Pig class
        self.Pig_list = []
        pig = Pig()
        self.Pig_list.append(pig)
        #make Chicken class
        self.Chic_list = []
        chic = Chicken()
        self.Chic_list.append(chic)

        #make all BBQ list
        self.Beef_list_sprite = arcade.SpriteList()
        self.Pig_list_sprite = arcade.SpriteList()
        self.Chic_list_sprite = arcade.SpriteList()
        self.All_BBQ_list = arcade.SpriteList()

        #initialize stove status and stove position and What on stove
        self.stove_status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.stove_position = [60, 100, 140, 183, 226, 266, 306, 343, 382, 423]
        self.what_on_stove = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 0 = Nothing ,1 = Beef ,2 = Pig ,3 = Chicken
        self.beef_on_stove = []
        self.pig_on_stove = []
        self.chic_on_stove = []
        #Roasting time
        self.roasting_time = roasting
        #make a bag
        self.bag = Bag(self,670,270)

   
    def on_mouse_press(self,x,y,buttons,modifiers):
        if self.player.hit(self.button1,20):
            for i in range(len(self.stove_status)): 
                if self.stove_status[i]==1: #check stove status before push a BBQ
                    continue
                self.stove_status[i] = 1 #stove i is not availble
                self.what_on_stove[i] = 1 #beef is on stove i
                self.Beef_sprite = arcade.Sprite("image/BeefRare.png")
                self.Beef_sprite.set_position(self.stove_position[i],100) #Beef n
                beef_on_stove = self.stove_position[i] #Beef n is on position i
                break
            #contend Beef to list.
            self.Beef_list.append(Beef())
            self.Beef_list_sprite.append(self.Beef_sprite)
            self.All_BBQ_list.append(self.Beef_sprite)
            self.beef_on_stove.append(beef_on_stove)


        if self.player.hit(self.button2,20):
            for i in range(len(self.stove_status)):
                if self.stove_status[i]==1:
                    continue
                self.stove_status[i] = 1
                self.what_on_stove[i] = 2
                Pig_sprite = arcade.Sprite("image/PigRare.png")
                Pig_sprite.set_position(self.stove_position[i],100)
                pig_on_stove = self.stove_position[i]
                break
            #contend Pig to list.
            self.Pig_list.append(Pig())
            self.Pig_list_sprite.append(Pig_sprite)
            self.All_BBQ_list.append(Pig_sprite)
            self.pig_on_stove.append(pig_on_stove)

        if self.player.hit(self.button3,20):
            for i in range(len(self.stove_status)):
                if self.stove_status[i]==1:
                    continue
                self.stove_status[i] = 1
                self.what_on_stove[i] = 3
                Chic_sprite = arcade.Sprite("image/ChicRare.png")
                Chic_sprite.set_position(self.stove_position[i],100)
                chic_on_stove = self.stove_position[i]
                break
            #contend Chicken to list.
            self.Chic_list.append(Chicken()) 
            self.Chic_list_sprite.append(Chic_sprite)     
            self.All_BBQ_list.append(Chic_sprite)
            self.chic_on_stove.append(chic_on_stove)

        #Pick up BBQ from the stove
        if len(self.Beef_list_sprite) != 0:
            for i in range(len(self.Beef_list_sprite)):
                if abs(self.player.x - self.Beef_list_sprite[i].center_x) <= 20 and abs(self.player.y - self.Beef_list_sprite[i].center_y) <= 20 :
                    for n in range(len(self.beef_on_stove)):
                        if self.beef_on_stove[n] == self.Beef_list_sprite[i].center_x:
                            for d in range(len(self.stove_position)):
                                if self.beef_on_stove[n] == self.stove_position[d]:
                                    self.stove_status[d] = 0
                                    self.what_on_stove[d] = 0
                                    break
                            del self.beef_on_stove[n]
                            break    
                    self.Beef_list_sprite[i].kill()
                    break

        if len(self.Pig_list_sprite) != 0:
            for i in range(len(self.Pig_list_sprite)):
                if abs(self.player.x - self.Pig_list_sprite[i].center_x) <= 20 and abs(self.player.y - self.Pig_list_sprite[i].center_y) <= 20 :
                    for n in range(len(self.pig_on_stove)):
                        if self.pig_on_stove[n] == self.Pig_list_sprite[i].center_x:
                            for d in range(len(self.stove_position)):
                                if self.pig_on_stove[n] == self.stove_position[d]:
                                    self.stove_status[d] = 0
                                    self.what_on_stove[d] = 0
                                    break
                            del self.pig_on_stove[n]
                            break
                    self.Pig_list_sprite[i].kill()
                    break

        if len(self.Chic_list_sprite) != 0:
            for i in range(len(self.Chic_list_sprite)):
                if abs(self.player.x - self.Chic_list_sprite[i].center_x) <= 20 and abs(self.player.y - self.Chic_list_sprite[i].center_y) <= 20 :
                    for n in range(len(self.chic_on_stove)):
                        if self.chic_on_stove[n] == self.Chic_list_sprite[i].center_x:
                            for d in range(len(self.stove_position)):
                                if self.chic_on_stove[n] == self.stove_position[d]:
                                    self.stove_status[d] = 0
                                    self.what_on_stove[d] = 0
                                    break
                            del self.chic_on_stove[n]
                            break
                    self.Chic_list_sprite[i].kill()
                    break
            
    def update(self,delta):

        for n in range(len(self.stove_status)):
            if self.stove_status[n]==0 and self.what_on_stove[n]==0: #Check stove status and what on stove "Nothing -->continue"
                continue
            N = n # N is current position.
            if self.what_on_stove[n]==1 :#Stove's position n is beef

                if len(self.Beef_list_sprite) != 0:
                    for i in range(len(self.Beef_list_sprite)): #To check Beef_sprite in Beef_list_sprite is on position i ??
                        self.Beef_list[i].update(delta) #Update Beef()
                        Beef_sprite = self.Beef_list_sprite[i] #Decleration Beef_sprite as Beef_list_sprite i     
                        if Beef_sprite.center_x != self.stove_position[N]: #Check position of Beef_sprite(Beef_list_sprite i) 
                            continue
  
                        seconds = int(self.Beef_list[i].roasting_time) % 60
                        minutes = int(self.Beef_list[i].roasting_time) // 60
                        break
                    if seconds==0 or minutes<0 :
                        Beef_sprite.texture = arcade.load_texture("image/BeefWell.png")
                        Beef_sprite.changed = True

            elif self.what_on_stove[n]==2 :
                if len(self.Pig_list_sprite) != 0:
                    for i in range(len(self.Pig_list_sprite)): #To check Pig_sprite in Pig_list_sprite is on position i ??
                        self.Pig_list[i].update(delta) #Update Pig()
                        Pig_sprite = self.Pig_list_sprite[i] #Decleration Pig_sprite as Pig_list_sprite i     
                        if Pig_sprite.center_x != self.stove_position[N]: #Check position of Pig_sprite(Pig_list_sprite i) 
                            continue

                        seconds = int(self.Pig_list[i].roasting_time) % 60
                        minutes = int(self.Pig_list[i].roasting_time) // 60
                        break
                    if seconds==0 or minutes<0 :
                        Pig_sprite.texture = arcade.load_texture("image/PigWell.png")
                        Pig_sprite.changed = True

            elif self.what_on_stove[n]==3 :
                if len(self.Chic_list_sprite) != 0:
                    for i in range(len(self.Chic_list_sprite)): #To check Chic_sprite in Chic_list_sprite is on position i ??
                        self.Chic_list[i].update(delta) #Update Chicken()
                        Chic_sprite = self.Chic_list_sprite[i] #Decleration Chic_sprite as Chic_list_sprite i     
                        if Chic_sprite.center_x != self.stove_position[N]: #Check position of Chic_sprite(Chic_list_sprite i) 
                            continue

                        seconds = int(self.Chic_list[i].roasting_time) % 60
                        minutes = int(self.Chic_list[i].roasting_time) // 60
                        break
                    if seconds==0 or minutes<0 :
                        Chic_sprite.texture = arcade.load_texture("image/ChicWell.png")
                        Chic_sprite.changed = True

        
