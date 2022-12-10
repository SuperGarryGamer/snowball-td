from GameObject import GameObject

class Button(GameObject):
    def __init__(self, game, x, y, img_path, onclick):
        super().__init__(game, x, y, img_path)
        self.onclick = onclick