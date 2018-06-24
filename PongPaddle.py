from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty
from kivy.vector import Vector

class PongPaddle(Widget):
    score = NumericProperty(0)
    win_count = NumericProperty(0)
    name = StringProperty('')

    def bounce_ball(self, ball, velocity_multiplier):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            
            #set threshold for velocity
            if (bounced.x < 20 and bounced.x > -20):
                vel = bounced * velocity_multiplier
                ball.velocity = vel.x, vel.y + offset
            else:
                ball.velocity = bounced.x, bounced.y + offset