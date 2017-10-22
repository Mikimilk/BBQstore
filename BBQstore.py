import arcade
import random
from Actor import World,Player,Stove1,Stove2,Stove3,Stove4,Stove5,Stove6,Stove7,Stove8,Stove9,Stove10,Model,Collectable,Beef,Pig,Chicken,Bag
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
        self.world = World(width, height)
        self.background = arcade.load_texture("image/Background.png") 
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
        #initialize Bag
        self.Bag_sprite = ModelSprite("image/Bag.png",model=self.world.bag)


    def on_mouse_motion(self, x, y, dx, dy):
        self.world.player.on_mouse_motion(x, y, dx, dy)


    #def on_mouse_drag(self,x, y, dx, dy, buttons, modifiers):
        #self.world.player.on_mouse_drag(x, y, dx, dy, buttons, modifiers)

    def on_mouse_press(self,x,y,buttons,modifiers):
        #Check player hit button
        self.world.on_mouse_press(x,y,buttons,modifiers)

    def on_draw(self):
        arcade.start_render()  
        arcade.draw_texture_rectangle(SCREEN_WIDTH//2 , SCREEN_HEIGHT//2 ,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        #draw bag
        self.Bag_sprite.draw()
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
        self.world.All_BBQ_list.draw()

        #draw player
        self.player_sprite.draw()
        

    def update(self,delta):
        
        self.world.update(delta)

 
if __name__ == '__main__':
    window = BBQwindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
