import random

def Shooter(GameObject):
    def __init__(self):
        super.__init__(self, game, x, y, img_path, visible=True, collision=True)
        self.health=40
    def shoot(self):
        self.game.currScene.add_obj("snowball" + str(random.randint(0, 10000)), Snowball(self.game,self.limg.x,self.limg.y,'assets/snowball.png'))
    def on_death(self):
        if health<=0:
            for obj in self.game.currScene.objects.keys:
                if self.game.currScene.objects[obj] is self:
                    del(self.game.currScene.objects[self.game.currScene.objects.keys])
    def collision(self,object):
        if self.limg.colliderect(object.get_rect())==True:
            self.health=self.health-1
