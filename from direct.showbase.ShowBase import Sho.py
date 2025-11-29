from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
 
class Game(ShowBase):
    def _init_(self):
        ShowBase._init_(self)
        self.land = Mapmanager()
        base.camLens.setFov(90)
 
game = Game()
game.run()