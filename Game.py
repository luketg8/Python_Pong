from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty
from kivy.vector import Vector
from kivy.clock import Clock   
import PongMenu
import PongGame     

class PongGameBuilder(App):
    def build(self):
        game = PongGame.PongGame()
        game.initialise(self.difficulty, self.paddle_height, self.player_name)
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        self.popup = Popup(title='Pong', content=game, auto_dismiss=False)
        self.popup.open()

    def set_name(self, name):
        self.player_name = name
        
    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    def set_paddle_height(self, height):
        self.paddle_height = height

class PongApp(App):
    def build(self):
        menu = PongMenu.PongMenu()
        return menu

if __name__ == '__main__':
    PongApp().run()