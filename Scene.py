import GameObject
#
class Scene:
    objects = {}

    def add_obj(self, id, obj):
        self.objects[id] = obj

    def __init__(self, objects = {}):
        self.objects = objects