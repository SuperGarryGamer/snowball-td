import GameObject

class Burglar(GameObject):
    def __init__(self, game, x, y, w, h, img_path, visible=True, collision=True, damage=10):
        super.__init__(game, x, y, w, h, img_path, visible, collision)
        self.damage = damage