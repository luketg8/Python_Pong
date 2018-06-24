from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty
import PongBall
import PongPaddle

class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def initialise(self, difficulty, height, playername, playername2):
        self.difficulty = difficulty
        #divide the size of the ball by the difficulty (higher difficulty, lower size)
        self.ball.size = [x / difficulty for x in self.ball.size]
        self.velocity_multiplier = 1 + (difficulty *.1)

        #set the height of the paddles
        self.player1.size = (25, height)
        self.player2.size = (25, height)
        
        #set the name of the player
        self.player1.name = playername
        self.player2.name = playername2

        #start the game
        self.serve_ball()

    def serve_ball(self, vel=(4, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):
        self.ball.move()

        # bounce off the paddles
        self.player1.bounce_ball(self.ball, self.velocity_multiplier)
        self.player2.bounce_ball(self.ball, self.velocity_multiplier)

        # bounce ball off bottom or top
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1

        # check if point scored
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

if __name__ == '__main__':
    PongGame()