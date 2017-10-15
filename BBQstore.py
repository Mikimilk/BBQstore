import arcade
import random
from Actor2 import World,Player,Stove1,Stove2,Stove3,Stove4,Stove5,Stove6,Stove7,Stove8,Stove9,Stove10,Model,Collectable,Beef,Pig,Chicken
from pyglet.window import mouse

roasting = 5
SCREEN_WIDTH = 760
SCREEN_HEIGHT = 550

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
 
        super().__init__(*args, **kwargs)
 
    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
 
    def draw(self):
        self.sync_with_model()
        super().draw()

 
class BBQwindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.PINK)
        self.world = World(width, height) 
        #initialize player
        self.player_sprite = ModelSprite("image/hand1.png",model=self.world.player)

        #initialize stove
        self.Stove1_sprite = ModelSprite("image/ApieceofStove/images/Stove_01.jpg",model=self.world.stove1) 
        self.Stove2_sprite = ModelSprite("image/ApieceofStove/images/Stove_02.jpg",model=self.world.stove2)
        self.Stove3_sprite = ModelSprite("image/ApieceofStove/images/Stove_03.jpg",model=self.world.stove3)
        self.Stove4_sprite = ModelSprite("image/ApieceofStove/images/Stove_04.jpg",model=self.world.stove4)
        self.Stove5_sprite = ModelSprite("image/ApieceofStove/images/Stove_05.jpg",model=self.world.stove5)
        self.Stove6_sprite = ModelSprite("image/ApieceofStove/images/Stove_06.jpg",model=self.world.stove6)
        self.Stove7_sprite = ModelSprite("image/ApieceofStove/images/Stove_07.jpg",model=self.world.stove7)
        self.Stove8_sprite = ModelSprite("image/ApieceofStove/images/Stove_08.jpg",model=self.world.stove8)
        self.Stove9_sprite = ModelSprite("image/ApieceofStove/images/Stove_09.jpg",model=self.world.stove9)
        self.Stove10_sprite = ModelSprite("image/ApieceofStove/images/Stove_10.jpg",model=self.world.stove10) 
        
        #initialize button
        self.Button1_sprite = ModelSprite("image/Button1.png",model=self.world.button1)
        self.Button2_sprite = ModelSprite("image/Button2.png",model=self.world.button2)
        self.Button3_sprite = ModelSprite("image/Button3.png",model=self.world.button3)

        #initialize BBQ
        self.Beef_list = arcade.SpriteList()
        self.BeefW_list = arcade.SpriteList()
        self.Pig_list = arcade.SpriteList()
        self.PigW_list = arcade.SpriteList()
        self.Chic_list = arcade.SpriteList()
        self.ChicW_list = arcade.SpriteList()
        
        #initialize_time_roasting
        self.roast_time = roasting

    def on_mouse_motion(self, x, y, dx, dy):
        self.world.player.on_mouse_motion(x, y, dx, dy)


    #def on_mouse_drag(self,x, y, dx, dy, buttons, modifiers):
        #self.world.on_mouse_drag(x, y, dx, dy, buttons, modifiers)

    def on_mouse_press(self,x,y,buttons,modifiers):
        #Check player hit button
        if self.world.player.hit(self.world.button2, 20):
            print("press button2.")
            pig = Pig("image/PigRare.png", 1)
            pig.center_x = self.world.stove2.x
            pig.center_y = self.world.stove2.y
            # Add the Pig to the appropriate lists
            self.Pig_list.append(pig)
            print("Pig iss on stove")

        elif self.world.player.hit(self.world.button1, 20):
            print("press button1.")
            beef = Beef("image/BeefRare.png", 1)
            beef.center_x = self.world.stove1.x
            beef.center_y = self.world.stove1.y
            # Add the Beef to the appropriate lists
            self.Beef_list.append(beef)

        elif self.world.player.hit(self.world.button3, 20):
            print("press button3.")
            chic = Chicken("image/ChicRare.png", 1)
            chic.center_x = self.world.stove3.x
            chic.center_y = self.world.stove3.y
            # Add the Chic to the appropriate lists
            self.Chic_list.append(chic)

    def on_draw(self):
        arcade.start_render()  
        #draw all a piece of stove.
        self.Stove1_sprite.draw()
        self.Stove2_sprite.draw()
        self.Stove3_sprite.draw()
        self.Stove4_sprite.draw()
        self.Stove5_sprite.draw()
        self.Stove6_sprite.draw()
        self.Stove7_sprite.draw()
        self.Stove8_sprite.draw()
        self.Stove9_sprite.draw()
        self.Stove10_sprite.draw()

        #draw all Button
        self.Button1_sprite.draw()
        self.Button2_sprite.draw()
        self.Button3_sprite.draw()

        #draw all BBQ
        self.Beef_list.draw()

        #draw player
        self.player_sprite.draw()
        

    def update(self,delta):
        
        self.world.update(delta)

        stove2_status = \
            arcade.check_for_collision_with_list(self.Stove2_sprite,
                                                 self.Pig_list)
        for pig in stove2_status:    
            # Position of Beef
            pig.center_x = self.world.stove2.x
            pig.center_y = self.world.stove2.y
            #Swap beefrare to beef well.
            self.roast_time -= delta
            seconds = int(self.roast_time) % 60
            minutes = int(self.roast_time) // 60
            if seconds==0 or minutes<0 :
                pig.texture = arcade.load_texture("image/PigWell.png")
                pig.changed = True
                # Add the Pig to the appropriate lists
                self.PigW_list.append(pig)


        stove1_status = \
            arcade.check_for_collision_with_list(self.Stove1_sprite,
                                                 self.Beef_list)
        for beef in stove1_status:    
            # Position of Beef
            beef.center_x = self.world.stove1.x
            beef.center_y = self.world.stove1.y
            #Swap beef rare to beef well.
            self.roast_time -= delta
            seconds = int(self.roast_time) % 60
            minutes = int(self.roast_time) // 60
            if seconds==0 or minutes<0 :
                beef.texture = arcade.load_texture("image/BeefWell.png")
                beef.changed = True
                # Add the Beef to the appropriate lists
                self.BeefW_list.append(beef)

        
        stove3_status = \
            arcade.check_for_collision_with_list(self.Stove3_sprite,
                                                 self.Chic_list)
        for chic in stove3_status:    
            # Position of Beef
            chic.center_x = self.world.stove3.x
            chic.center_y = self.world.stove3.y
            #Swap beefrare to beef well.
            self.roast_time -= delta
            seconds = int(self.roast_time) % 60
            minutes = int(self.roast_time) // 60
            if seconds==0 or minutes<0 :
                chic.texture = arcade.load_texture("image/ChicWell.png")
                chic.changed = True
                # Add the Chic to the appropriate lists
                self.ChicW_list.append(chic)


 
if __name__ == '__main__':
    window = BBQwindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
