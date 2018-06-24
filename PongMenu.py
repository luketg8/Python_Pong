from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty
from Game import PongGameBuilder

class PongMenu(Widget):
    def set_easy(self):
        #start the game with an easy difficulty
        game = PongGameBuilder()

        #set the desired properties
        game.set_difficulty(1)

        #start the game
        self.start_game(game)

    def set_hard(self):
        #start the game with a hard difficulty
        game = PongGameBuilder()

        #set the desired properties
        game.set_difficulty(2)

        #start the game
        self.start_game(game)

    def start_game(self, game):
        game.set_paddle_height(self.paddle_slider.value)
        game.set_names(self.player_name.text, self.player2_name.text)
        game.run()

if __name__ == '__main__':
    PongMenu()