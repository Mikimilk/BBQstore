import arcade
from random import randint
from pyglet.window import mouse
import time
roasting = 5.0
gametime = 60.0
OrderCome = 30.0
Score_for_rare_BBQ = 7
Score_for_well_BBQ = 10
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
        self.Finish_Beef_list = 0
        self.Finish_Pig_list = 0
        self.Finish_Chic_list = 0
    def update(self,delta):
        pass

class Bin(Model):
    def __init__(self, world ,x ,y):
        super().__init__(world ,x ,y)

    def update(self,delta):
        pass

class Order:
    def __init__(self):
        super().__init__()
        self.changed = False
        self.order_time = randint(20,30)
        self.Beef_Order = randint(1,4)
        self.Pig_Order = randint(1,4)
        self.Chic_Order = randint(1,4)
    def update(self,delta):
        self.order_time -= delta

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
        self.stove1 = Stove1(self,59,84) 
        self.stove2 = Stove2(self,116,84) 
        self.stove3 = Stove3(self,153,84) 
        self.stove4 = Stove4(self,190,84)
        self.stove5 = Stove5(self,228,84) 
        self.stove6 = Stove6(self,267,84) 
        self.stove7 = Stove7(self,306,84) 
        self.stove8 = Stove8(self,347,84) 
        self.stove9 = Stove9(self,387,84) 
        self.stove10 = Stove10(self,447,84)
        #make buttons
        self.button1 = Button1(self,345,174)
        self.button2 = Button2(self,265,170)
        self.button3 = Button3(self,185,172)
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
        self.stove_position = [77, 116, 153, 190, 228, 267, 306, 347, 387, 430]
        self.what_on_stove = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 0 = Nothing ,1 = Beef ,2 = Pig ,3 = Chicken
        self.beef_on_stove = []
        self.pig_on_stove = []
        self.chic_on_stove = []
        #Roasting time
        self.roasting_time = roasting

        #make a bag
        self.bag = Bag(self,670,270)

        #make a bin
        self.bin = Bin(self,640,45)

        #make Order
        #Order sprite
        self.Order_come = OrderCome #Inter-arrival time each order comes.
        self.Order_position_x = [125,410,220]
        self.Order_position_y = [440,415,315]
        self.order = Order()
        self.Order_sprite_list = arcade.SpriteList()
        for i in range(3):
            Order_sprite = arcade.Sprite("image/Order.png")
            Order_sprite.set_position(self.Order_position_x[i],self.Order_position_y[i])
            self.Order_sprite_list.append(Order_sprite)

        self.choose_Order = arcade.SpriteList()
        self.current_order = 0 # 0 = Not yet choose ,1 = choose order1 ,2 = choose order2 ,3 = choose order3   
        
        #Order text
        self.Draw_text_order_list = []
        self.Beef_Order_list = []
        self.Pig_Order_list = []
        self.Chic_Order_list = []
        for i in range(3):
            self.Draw_text_order = True
            self.Draw_text_order_list.append(self.Draw_text_order)

            self.Beef_Order = randint(1,4)
            self.Pig_Order = randint(1,4)
            self.Chic_Order = randint(1,4)
            self.Beef_Order_list.append(self.Beef_Order)
            self.Pig_Order_list.append(self.Pig_Order)
            self.Chic_Order_list.append(self.Chic_Order)

        for i in range(3):
            if self.Draw_text_order_list[i]:
                if i==0:
                    Beef_order = f"Beef: {self.Beef_Order_list[0]}"
                    self.Beef_order1 = arcade.create_text(Beef_order , arcade.color.BLACK, 17)
                    Pig_order = f"Pork: {self.Pig_Order_list[0]}"
                    self.Pig_order1 = arcade.create_text(Pig_order , arcade.color.BLACK, 17)
                    Chic_order = f"Chicken: {self.Chic_Order_list[0]}"
                    self.Chic_order1 = arcade.create_text(Chic_order , arcade.color.BLACK, 17)

                if i==1:
                    Beef_order = f"Beef: {self.Beef_Order_list[1]}"
                    self.Beef_order2 = arcade.create_text(Beef_order , arcade.color.BLACK, 17)
                    Pig_order = f"Pork: {self.Pig_Order_list[1]}"
                    self.Pig_order2 = arcade.create_text(Pig_order , arcade.color.BLACK, 17)
                    Chic_order = f"Chicken: {self.Chic_Order_list[1]}"
                    self.Chic_order2 = arcade.create_text(Chic_order , arcade.color.BLACK, 17)

                if i==2:
                    Beef_order = f"Beef: {self.Beef_Order_list[2]}"
                    self.Beef_order3 = arcade.create_text(Beef_order , arcade.color.BLACK, 17)
                    Pig_order = f"Pork: {self.Pig_Order_list[2]}"
                    self.Pig_order3 = arcade.create_text(Pig_order , arcade.color.BLACK, 17)
                    Chic_order = f"Chicken: {self.Chic_Order_list[2]}"
                    self.Chic_order3 = arcade.create_text(Chic_order , arcade.color.BLACK, 17)

        #Initialize variables to count scores.
        self.Count_beef_cooked = [] #check how Beef BBQ cooked?? -> 0 = rare , 1 = well done
        self.Count_pig_cooked = []
        self.Count_chic_cooked = [] 
        self.Count_beef_score = 0
        self.Count_pig_score = 0
        self.Count_chic_score = 0
        self.Calculate_order = 0
        self.Total_score = 0

    def on_mouse_press(self,x,y,buttons,modifiers):
    #Push BBQ to the stove
        if self.player.hit(self.button1,20):
            for i in range(len(self.stove_status)): 
                if self.stove_status[i]==1: #To check stove status before push a BBQ
                    continue
                self.stove_status[i] = 1 #stove i is not availble
                self.what_on_stove[i] = 1 #beef is on stove i
                self.Beef_sprite = arcade.Sprite("image/BeefRare.png")
                self.Beef_sprite.set_position(self.stove_position[i],80) #Beef n
                beef_on_stove = self.stove_position[i] #Beef n is on position i
                Count_beef_rare = 0 #To keep how beef BBQ cooked.
                break
            #contend Beef to list.
            self.Beef_list.append(Beef())
            self.Beef_list_sprite.append(self.Beef_sprite)
            self.All_BBQ_list.append(self.Beef_sprite)
            self.beef_on_stove.append(beef_on_stove)
            self.Count_beef_cooked.append(Count_beef_rare)


        if self.player.hit(self.button2,20):
            for i in range(len(self.stove_status)):
                if self.stove_status[i]==1:
                    continue
                self.stove_status[i] = 1
                self.what_on_stove[i] = 2
                self.Pig_sprite = arcade.Sprite("image/PigRare.png")
                self.Pig_sprite.set_position(self.stove_position[i],80)
                pig_on_stove = self.stove_position[i]
                Count_pig_rare = 0
                break
            #contend Pig to list.
            self.Pig_list.append(Pig())
            self.Pig_list_sprite.append(self.Pig_sprite)
            self.All_BBQ_list.append(self.Pig_sprite)
            self.pig_on_stove.append(pig_on_stove)
            self.Count_pig_cooked.append(Count_pig_rare)

        if self.player.hit(self.button3,20):
            for i in range(len(self.stove_status)):
                if self.stove_status[i]==1:
                    continue
                self.stove_status[i] = 1
                self.what_on_stove[i] = 3
                self.Chic_sprite = arcade.Sprite("image/ChicRare.png")
                self.Chic_sprite.set_position(self.stove_position[i],76)
                chic_on_stove = self.stove_position[i]
                Count_chic_rare = 0
                break
            #contend Chicken to list.
            self.Chic_list.append(Chicken()) 
            self.Chic_list_sprite.append(self.Chic_sprite)     
            self.All_BBQ_list.append(self.Chic_sprite)
            self.chic_on_stove.append(chic_on_stove)
            self.Count_chic_cooked.append(Count_chic_rare)

    #Pick up BBQ from the stove and send to a bag.
        if len(self.Beef_list_sprite) != 0:
            for i in range(len(self.Beef_list_sprite)): #To kill member of Beef_list_sprite
                if abs(self.player.x - self.Beef_list_sprite[i].center_x) <= 20 and abs(self.player.y - self.Beef_list_sprite[i].center_y) <= 20 :
                    for n in range(len(self.beef_on_stove)): #To set status of stove AND delete member of beef_on_stove
                        if self.beef_on_stove[n] == self.Beef_list_sprite[i].center_x:
                            for d in range(len(self.stove_position)): 
                                if self.beef_on_stove[n] == self.stove_position[d]:
                                    self.stove_status[d] = 0
                                    self.what_on_stove[d] = 0
                                    break
                            del self.beef_on_stove[n]
                            break    
                    self.bag.Finish_Beef_list += 1 #To keep beef BBQ into bag.
                    self.Beef_list_sprite[i].kill()

                    if self.Count_beef_cooked[i] == 0:
                        self.Count_beef_score += Score_for_rare_BBQ
                    else :
                        self.Count_beef_score += Score_for_well_BBQ
                    self.Calculate_order += self.Count_beef_score
                    del self.Count_beef_cooked[i]
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
                    self.bag.Finish_Pig_list += 1 #To keep pork BBQ into bag.
                    self.Pig_list_sprite[i].kill()

                    if self.Count_pig_cooked[i] == 0:
                        self.Count_pig_score += Score_for_rare_BBQ
                    else :
                        self.Count_pig_score += Score_for_well_BBQ
                    self.Calculate_order += self.Count_pig_score
                    del self.Count_pig_cooked[i]
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
                    self.bag.Finish_Chic_list += 1 #To keep chicken BBQ into bag.
                    self.Chic_list_sprite[i].kill()

                    if self.Count_chic_cooked[i] == 0:
                        self.Count_chic_score += Score_for_rare_BBQ
                    else :
                        self.Count_chic_score += Score_for_well_BBQ
                    self.Calculate_order += self.Count_chic_score
                    del self.Count_chic_cooked[i]
                    break

    #Choose Order
        if len(self.choose_Order)==0 :
            for i in range(3):
                if abs(self.player.x - self.Order_sprite_list[i].center_x) <= 100 and abs(self.player.y - self.Order_sprite_list[i].center_y) <= 100 :
                    choose_Order = arcade.Sprite("image/Press_Order.png")
                    choose_Order.set_position(self.Order_position_x[i],self.Order_position_y[i])
                    self.choose_Order.append(choose_Order)
                    self.current_order = i+1
                    break

    #Sell BBQ
        if self.player.hit(self.bag , 100):
            for i in range(3):
                if self.current_order == i+1 :
                    if self.bag.Finish_Beef_list == self.Beef_Order_list[i] and self.bag.Finish_Pig_list == self.Pig_Order_list[i] and self.bag.Finish_Chic_list == self.Chic_Order_list[i] :
                        self.bag.Finish_Beef_list = 0
                        self.bag.Finish_Pig_list = 0
                        self.bag.Finish_Chic_list = 0
                        self.Total_score += self.Calculate_order 
                        self.Calculate_order = 0
                        self.Count_beef_score = 0
                        self.Count_pig_score = 0
                        self.Count_chic_score = 0
                        self.Draw_text_order_list[i] = False
                        self.choose_Order[0].kill()
                        self.current_order = 0

    #Get rid of BBQ
        if self.player.hit(self.bin, 100):
            self.bag.Finish_Beef_list = 0
            self.bag.Finish_Pig_list = 0
            self.bag.Finish_Chic_list = 0
            self.Calculate_order = 0

    def update(self,delta):

        #RoastBBQ
        for n in range(len(self.stove_status)):
            if self.stove_status[n]==0 and self.what_on_stove[n]==0: #Check stove status and what on stove "Nothing -->continue"
                continue
            N = n # N is current position.
            if self.what_on_stove[n]==1 :#Stove's position n is beef
                if len(self.Beef_list_sprite) != 0:
                    for i in range(len(self.Beef_list_sprite)): #To check Beef_sprite in Beef_list_sprite is on position i ??
                        Beef_sprite = self.Beef_list_sprite[i] #Decleration Beef_sprite as Beef_list_sprite i     
                        Count_beef_well = self.Count_beef_cooked[i]
                        if Beef_sprite.center_x != self.stove_position[N]: #Check position of Beef_sprite(Beef_list_sprite i) 
                            continue
                        self.Beef_list[i].update(delta) #Update Beef()
                        seconds = int(self.Beef_list[i].roasting_time) % 60
                        minutes = int(self.Beef_list[i].roasting_time) // 60
                        break
                    if seconds==0 or minutes<0 :
                        Beef_sprite.texture = arcade.load_texture("image/BeefWell.png")
                        Beef_sprite.changed = True
                        Count_beef_well = 1 
                        break

            elif self.what_on_stove[n]==2 :
                if len(self.Pig_list_sprite) != 0:
                    for i in range(len(self.Pig_list_sprite)): #To check Pig_sprite in Pig_list_sprite is on position i ??
                        self.Pig_list[i].update(delta) #Update Pig()
                        Pig_sprite = self.Pig_list_sprite[i] #Decleration Pig_sprite as Pig_list_sprite i   
                        Count_pig_well = self.Count_pig_cooked[i]  
                        if Pig_sprite.center_x != self.stove_position[N]: #Check position of Pig_sprite(Pig_list_sprite i) 
                            continue

                        seconds = int(self.Pig_list[i].roasting_time) % 60
                        minutes = int(self.Pig_list[i].roasting_time) // 60
                        break
                    if seconds==0 or minutes<0 :
                        Pig_sprite.texture = arcade.load_texture("image/PigWell.png")
                        Pig_sprite.changed = True
                        Count_pig_well = 1
                        break

            elif self.what_on_stove[n]==3 :
                if len(self.Chic_list_sprite) != 0:
                    for i in range(len(self.Chic_list_sprite)): #To check Chic_sprite in Chic_list_sprite is on position i ??
                        self.Chic_list[i].update(delta) #Update Chicken()
                        Chic_sprite = self.Chic_list_sprite[i] #Decleration Chic_sprite as Chic_list_sprite i  
                        Count_chic_well = self.Count_chic_cooked[i]
                        if Chic_sprite.center_x != self.stove_position[N]: #Check position of Chic_sprite(Chic_list_sprite i) 
                            continue

                        seconds = int(self.Chic_list[i].roasting_time) % 60
                        minutes = int(self.Chic_list[i].roasting_time) // 60
                        break
                    if seconds==0 or minutes<0 :
                        Chic_sprite.texture = arcade.load_texture("image/ChicWell.png")
                        Chic_sprite.changed = True
                        Count_beef_well = 1
                        break

        #Order_Coming
        for i in range(3):
            if not self.Draw_text_order_list[i]:
                self.Order_come -= 1
                if self.Order_come == 0:
                    self.Draw_text_order_list[i] = True
                    self.Order_come = 30.0
                    self.Beef_Order = randint(1,4)
                    self.Pig_Order = randint(1,4)
                    self.Chic_Order = randint(1,4)
                    self.Beef_Order_list.append(self.Beef_Order)
                    self.Pig_Order_list.append(self.Pig_Order)
                    self.Chic_Order_list.append(self.Chic_Order)
                    if i==0:
                        Beef_order = f"Beef: {self.Beef_Order_list[0]}"
                        self.Beef_order1 = arcade.create_text(Beef_order , arcade.color.BLACK, 17)
                        Pig_order = f"Pork: {self.Pig_Order_list[0]}"
                        self.Pig_order1 = arcade.create_text(Pig_order , arcade.color.BLACK, 17)
                        Chic_order = f"Chicken: {self.Chic_Order_list[0]}"
                        self.Chic_order1 = arcade.create_text(Chic_order , arcade.color.BLACK, 17)

                    if i==1:
                        Beef_order = f"Beef: {self.Beef_Order_list[1]}"
                        self.Beef_order2 = arcade.create_text(Beef_order , arcade.color.BLACK, 17)
                        Pig_order = f"Pork: {self.Pig_Order_list[1]}"
                        self.Pig_order2 = arcade.create_text(Pig_order , arcade.color.BLACK, 17)
                        Chic_order = f"Chicken: {self.Chic_Order_list[1]}"
                        self.Chic_order2 = arcade.create_text(Chic_order , arcade.color.BLACK, 17)

                    if i==2:
                        Beef_order = f"Beef: {self.Beef_Order_list[2]}"
                        self.Beef_order3 = arcade.create_text(Beef_order , arcade.color.BLACK, 17)
                        Pig_order = f"Pork: {self.Pig_Order_list[2]}"
                        self.Pig_order3 = arcade.create_text(Pig_order , arcade.color.BLACK, 17)
                        Chic_order = f"Chicken: {self.Chic_Order_list[2]}"
                        self.Chic_order3 = arcade.create_text(Chic_order , arcade.color.BLACK, 17)
