import pygame

class GameObject(pygame.sprite.Sprite):
    visible = True
    collision = True
    velocity = [0, 0]

    def __init__(self, game, x, y, img_path, visible=True,collision=True):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.img=pygame.image.load(img_path)
        self.limg = self.img.get_rect()
        self.limg.x=x
        self.limg.y=y
        self.collision = collision

    def setVisible(self, vis):
        self.visible = vis

    def setCollision(self, coll):
        self.collision = coll


