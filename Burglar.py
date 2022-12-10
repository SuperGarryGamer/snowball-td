import GameObject

class Burglar(GameObject):
    def __init__(self, game, x, y, img_path, visible=True, collision=True, damage=10):
        super.__init__(game, x, y, img_path,visible,collision)
        self.damage = damage
        self.velocity=[-7,0]
    def move(self):
        self.limg.x=self.limg.x+self.velocity[0]
        self.limg.y = self.limg.y + self.velocity[1]
    def on_House(self):
        if self.limg.x<=0:
            scene2=Scene()
            scene2.objects={"Game Over": GameObject(self.game,0,0,'assets/GameOverScreen.png')}