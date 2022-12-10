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
            self.setVisible(0)
            object.setVisible(0)



