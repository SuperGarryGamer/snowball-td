import pygame

class GameObject(pygame.sprite.Sprite):
    visible = True
    collision = True
    velocity = [0, 0]

    def __init__(self, game, x, y, w, h, img_path, visible=True, collision=True):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.rect = pygame.Rect(x, y, w, h)
        self.img = pygame.transform.scale(pygame.image.load(img_path), (w, h))
        self.collision = collision

    def setVisible(self, vis):
        self.visible = vis

    def setCollision(self, coll):
        self.collision = coll

    def setImage(self, img):
        self.img = pygame.transform.scale(img, (self.rect.w, self.rect.h))

    def tryMove(self, x, y):
        pass