def Snowball(GameObject):
    def __init__(self):
        super.__init__(self, game, x, y, img_path, visible=True,  collision=True)
        velocity=[5,0]
    def move(self):
        self.limg.x=self.limg.x + velocity[0]
        self.limg.y = self.limg.y + velocity[1]
    def collision(self,object):
        self.lobject=object.get_rect()
        if self.limg.colliderect(self.lobject)==True:
            for obj in self.game.currScene.objects.keys:
                if self.game.currScene.objects[obj] is object:
                    del(self.game.currScene.objects[self.game.currScene.objects.keys])

            for obj in self.game.currScene.objects.keys:
                if self.game.currScene.objects[obj] is self:
                    del(self.game.currScene.objects[self.game.currScene.objects.keys])



