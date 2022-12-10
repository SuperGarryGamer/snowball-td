import pygame
import time

from Button import Button
from Scene import Scene
from GameObject import GameObject

class Game:
    size = (640, 480)
    currScene = Scene({})

    def set_scene(self, scene):
        self.currScene = scene
        self._display_surf.fill(0)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

        self.currScene.add_obj("bg", GameObject(self, 0, 0, "./assets/TitleScreen.png"))
        self.currScene.add_obj("start", Button(self, 250, 200, "./assets/StartButton.png", lambda: print("asdfasdfasdf")))
        self.currScene.add_obj("exit", Button(self, 250, 300, "./assets/ExitButton.png", lambda: self.on_cleanup()))

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.KEYDOWN:
            pass
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for obj_k in self.currScene.objects.keys():
                obj = self.currScene.objects[obj_k]
                if event.pos[0] > obj.limg.x and event.pos[0] < obj.limg.x + obj.limg.w:
                    if event.pos[1] > obj.limg.y and event.pos[1] < obj.limg.y + obj.limg.h:
                        if isinstance(obj, Button):
                            obj.onclick()

            print(event)

    def on_loop(self):
        time.sleep(0.05)

    def on_render(self):
        self._display_surf.fill(0)
        for object in self.currScene.objects.values():
            if object.visible:
                self._display_surf.blit(object.img, object.limg)
        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()