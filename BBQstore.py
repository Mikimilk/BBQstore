import arcade
from random import randint
from Actor2 import World,Player,Stove1,Stove2,Stove3,Stove4,Stove5,Stove6,Stove7,Stove8,Stove9,Stove10,Model,Collectable,Beef,Pig,Chicken,Bag,Order
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
        self.background = arcade.load_texture("image/BGG.png") 
        #initialize player
        self.player_sprite = ModelSprite("image/hand1.png",model=self.world.player)

        #initialize stove
        self.Stove1_sprite = ModelSprite("image/ApieceofStove/Stove_01.png",model=self.world.stove1) 
        self.Stove2_sprite = ModelSprite("image/ApieceofStove/Stove_02.png",model=self.world.stove2)
        self.Stove3_sprite = ModelSprite("image/ApieceofStove/Stove_03.png",model=self.world.stove3)
        self.Stove4_sprite = ModelSprite("image/ApieceofStove/Stove_04.png",model=self.world.stove4)
        self.Stove5_sprite = ModelSprite("image/ApieceofStove/Stove_05.png",model=self.world.stove5)
        self.Stove6_sprite = ModelSprite("image/ApieceofStove/Stove_06.png",model=self.world.stove6)
        self.Stove7_sprite = ModelSprite("image/ApieceofStove/Stove_07.png",model=self.world.stove7)
        self.Stove8_sprite = ModelSprite("image/ApieceofStove/Stove_08.png",model=self.world.stove8)
        self.Stove9_sprite = ModelSprite("image/ApieceofStove/Stove_09.png",model=self.world.stove9)
        self.Stove10_sprite = ModelSprite("image/ApieceofStove/Stove_10.png",model=self.world.stove10) 
        
        #initialize button
        self.Button1_sprite = ModelSprite("image/Button1.png",model=self.world.button1)
        self.Button2_sprite = ModelSprite("image/Button2.png",model=self.world.button2)
        self.Button3_sprite = ModelSprite("image/Button3.png",model=self.world.button3)
        #initialize Bag
        self.Bag_sprite = ModelSprite("image/Bag.png",model=self.world.bag)
        #initialize Bin
        self.Bin_sprite = ModelSprite("image/Bin.png",model=self.world.bin)
        #make Game Time
        self.Game_Time = 60.0
        self.timer_text = None
        #make text position in each orders.
        self.Order_text_position_x = [[50,125,80],[345,420,370],[150,225,180]]
        self.Order_text_position_y = [[460,460,430],[430,430,400],[330,330,300]]
        

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

        #draw a bin
        self.Bin_sprite.draw()

        #draw all a piece of stove.
        self.Stove1_sprite.draw()
        self.Stove7_sprite.draw()
        self.Stove6_sprite.draw()
        self.Stove5_sprite.draw()
        self.Stove4_sprite.draw()
        self.Stove3_sprite.draw()
        self.Stove2_sprite.draw()
        self.Stove8_sprite.draw()
        self.Stove10_sprite.draw()
        self.Stove9_sprite.draw()

        #draw all Button
        self.Button1_sprite.draw()
        self.Button2_sprite.draw()
        self.Button3_sprite.draw()

        #draw all BBQ
        self.world.Beef_list_sprite.draw()
        self.world.Pig_list_sprite.draw()
        self.world.Chic_list_sprite.draw()

        #draw BBQ in bag.
        Beef = "Beef: {}".format(self.world.bag.Finish_Beef_list)
        arcade.draw_text(Beef,640,280, arcade.color.BLACK, 14)

        Pig = "Pork: {}".format(self.world.bag.Finish_Pig_list)
        arcade.draw_text(Pig,640,260, arcade.color.BLACK, 14)

        Chic = "Chicken: {}".format(self.world.bag.Finish_Chic_list)
        arcade.draw_text(Chic,640,240, arcade.color.BLACK, 14)

        #dram game time
        seconds = int(self.Game_Time) % 60
        minutes = int(self.Game_Time) // 60

        output = f"Time: {minutes:02d}:{seconds:02d}"
        self.timer_text = arcade.create_text(output, arcade.color.BLACK, 17)
        arcade.render_text(self.timer_text, 100, 510)

        #draw order
        for i in range(3):
            if self.world.Draw_text_order_list[i] :         
                self.world.Order_sprite_list[i].draw()


        #draw choose Order
        self.world.choose_Order.draw()

        #draw order text
        for n in range(3): #(order n) position(Beef,Pork,Chicken) 
            if self.world.Draw_text_order_list[n] : 
                if n==0:
                    arcade.render_text(self.world.Beef_order1 ,self.Order_text_position_x[n][0],self.Order_text_position_y[n][0])
                    arcade.render_text(self.world.Pig_order1 ,self.Order_text_position_x[n][1],self.Order_text_position_y[n][1])
                    arcade.render_text(self.world.Chic_order1 ,self.Order_text_position_x[n][2],self.Order_text_position_y[n][2])
                if n==1:
                    arcade.render_text(self.world.Beef_order2 ,self.Order_text_position_x[n][0],self.Order_text_position_y[n][0])
                    arcade.render_text(self.world.Pig_order2,self.Order_text_position_x[n][1],self.Order_text_position_y[n][1])
                    arcade.render_text(self.world.Chic_order2 ,self.Order_text_position_x[n][2],self.Order_text_position_y[n][2])
                if n==2:
                    arcade.render_text(self.world.Beef_order3 ,self.Order_text_position_x[n][0],self.Order_text_position_y[n][0])
                    arcade.render_text(self.world.Pig_order3 ,self.Order_text_position_x[n][1],self.Order_text_position_y[n][1])
                    arcade.render_text(self.world.Chic_order3 ,self.Order_text_position_x[n][2],self.Order_text_position_y[n][2])

        #draw score text
        output = f"Score: {self.world.Total_score}"
        self.score_text = arcade.create_text(output, arcade.color.BLACK, 17)
        arcade.render_text(self.score_text, 630, 510)

        #draw player
        self.player_sprite.draw()
        

    def update(self,delta):
        
        self.world.update(delta)
        self.Game_Time -= delta
 
if __name__ == '__main__':
    window = BBQwindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
