def Snowball(GameObject):
    def __init__(self, game, x, y, img_path, visible=True,  collision=True):
        super.__init__(self, game, x, y, img_path, visible,  collision)
        self.velocity=[5,0]
    def move(self):
        self.limg.x=self.limg.x + self.velocity[0]
        self.limg.y = self.limg.y + self.velocity[1]
    def collision(self,object):
        if self.limg.colliderect(object.get_rect())==True:
            for obj in self.game.currScene.objects.keys:
                if self.game.currScene.objects[obj] is object:
                    del(self.game.currScene.objects[self.game.currScene.objects.keys])

            for obj in self.game.currScene.objects.keys:
                if self.game.currScene.objects[obj] is self:
                    del(self.game.currScene.objects[self.game.currScene.objects.keys])



