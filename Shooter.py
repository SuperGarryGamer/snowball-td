import random

def Shooter(GameObject):
    def __init__(self):
        super.__init__(self, game, x, y, img_path, visible=True, collision=True)

    def shoot(self):
        self.game.currScene.add_obj("snowball" + str(random.randint(0, 10000)), Snowball(self.game,self.limg.x,self.limg.y,'assets/snowball.png'))
