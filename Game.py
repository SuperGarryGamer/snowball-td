import pygame
import time
import Scene

class Game:
    size = (640, 480)
    currScene = Scene()

    def set_scene(self, scene):
        self.currScene = scene
        self._display_surf.fill(0)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.KEYDOWN:
            pass

    def on_loop(self):
        pass

    def on_render(self):
        for object in self.currScene.objects.values():
            if object.visible:
                self._display_surf.blit(object.img, object.rect)
        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            self.on_loop()
            self.on_render()
        self.on_cleanup()