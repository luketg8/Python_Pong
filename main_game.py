from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty
from kivy.vector import Vector
from kivy.clock import Clock


class PongPaddle(Widget):
    score = NumericProperty(0)
    name = StringProperty('')

    def bounce_ball(self, ball, velocity_multiplier):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            
            if (bounced.x < 8 and bounced.x > -8):
                vel = bounced * velocity_multiplier
                ball.velocity = vel.x, vel.y + offset
            else:
                ball.velocity = bounced.x, bounced.y + offset


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class ChallengingPongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def initialise(self, difficulty, height, playername):
        self.difficulty = difficulty
        #divide the size of the ball by the difficulty (higher difficulty, lower size)
        self.ball.size = [x / difficulty for x in self.ball.size]
        self.velocity_multiplier = 1 + (difficulty *.1)

        #set the height of the paddles
        self.player1.size = (25, height)
        self.player2.size = (25, height)

        #set the name of the player
        self.player1.name = playername

        #start the game
        self.serve_ball()

    def serve_ball(self, vel=(4, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):
        self.ball.move()

        # bounce of paddles
        self.player1.bounce_ball(self.ball, self.velocity_multiplier)
        self.player2.bounce_ball(self.ball, self.velocity_multiplier)

        # bounce ball off bottom or top
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1

        # went of to a side to score point?
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball(vel=(4, 0))
        if self.ball.x > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-4, 0))

    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y

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
        game.set_name(self.player_name.text)
        game.run()
        

class PongGameBuilder(App):
    def build(self):
        game = PongGame()
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
        menu = PongMenu()
        return menu

if __name__ == '__main__':
    PongApp().run()