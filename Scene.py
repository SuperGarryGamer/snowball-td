import GameObject
#
class Scene:
    objects = {}

    def __init__(self, objects = {}):
        self.objects = objects