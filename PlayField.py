from Button import Button
from Scene import Scene


class PlayField(Scene):

    def __init__(self, objects, game):
        super().__init__(objects)
        self.game = game
        self.lines_y = [120, 240, 360]
        self.cannon_buy = Button(self.game, 0, 0, "./assets/cannon.png", lambda: self.game.pickup())
        self.add_obj("cannon_buy", self.cannon_buy)


