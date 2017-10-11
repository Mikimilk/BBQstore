import arcade
from Actor import World,Player,Beef,Pig,Chic,Plate,Tau
from pyglet.window import mouse

 
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
        self.Tau_sprite = ModelSprite("image/Tau.png",model=self.world.tau)   
        self.Plate_sprite = ModelSprite("image/Plate.png",model=self.world.plate)
        self.Beef_sprite = ModelSprite("image/BeefRare.png",model=self.world.beef)
        self.Pig_sprite = ModelSprite("image/PigRare.png",model=self.world.pig)
        self.Chic_sprite = ModelSprite("image/ChicRare.png",model=self.world.chic)
        self.BeefW_sprite = ModelSprite("image/BeefWell.png",model=self.world.beefW)
        self.PigW_sprite = ModelSprite("image/PigWell.png",model=self.world.pigW)
        self.ChicW_sprite = ModelSprite("image/ChicWell.png",model=self.world.chicW)   
        self.player_sprite = ModelSprite("image/hand1.png",model=self.world.player)


    def on_mouse_motion(self,x, y, dx, dy):
        self.world.player.on_mouse_motion(x, y, dx, dy)

    #def on_mouse_press(x, y, button, modifiers):
        #self.world.on_mouse_drag(x, y, buttons, modifiers)
    def on_mouse_drag(self,x, y, dx, dy, buttons, modifiers):
        self.world.on_mouse_drag(x, y, dx, dy, buttons, modifiers)
        self.world.player.on_mouse_drag(x, y, dx, dy, buttons, modifiers)

    def on_draw(self):
        arcade.start_render()  
        
        self.Tau_sprite.draw()
        self.Plate_sprite.draw()
        self.Beef_sprite.draw()
        self.Pig_sprite.draw()
        self.Chic_sprite.draw()
        self.BeefW_sprite.draw()
        self.PigW_sprite.draw()
        self.ChicW_sprite.draw()
        self.player_sprite.draw()

    def update(self,delta):
        
        self.world.update(delta)

 
if __name__ == '__main__':
    window = BBQwindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
