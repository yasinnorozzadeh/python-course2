import random
import arcade

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
SCREEN_TITLE = "Air Hockey"

class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.center_x = SCREEN_WIDTH//2
        self.center_y = SCREEN_HEIGHT//2
        self.color = arcade.color.GOLD
        self.radius = 20
        self.change_x = random.choice([1,-1])
        self.change_y = random.choice([1,-1])
        self.speed = 5
        self.width = self.radius * 2
        self.height = self.radius * 2

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, self.color)

    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

class Rocket(arcade.Sprite):
    def __init__(self, x, y, c):
        super().__init__()
        self.center_x = x
        self.center_y = y
        self.width = 10
        self.height = 80
        self.color = c
        self.change_x = 0
        self.change_y = 0
        self.speed = 5
        self.ball = Ball()
    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)

    def move(self):
        self.center_y += self.speed * self.change_y
        if self.center_y < 50:
            self.center_y = 50
        elif self.center_y > SCREEN_HEIGHT - 50:
            self.center_y = SCREEN_HEIGHT - 50

class Game(arcade.Window):
    def __init__(self):
        self.player1_score = 0
        self.player2_score = 0
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.ball = Ball()
        self.player1 = Rocket(SCREEN_WIDTH-15, SCREEN_HEIGHT/2,arcade.color.RED)
        self.player2 = Rocket(15, SCREEN_HEIGHT/2, arcade.color.BLUE)
        self.check = 0
    def on_draw(self):
        arcade.start_render()
        arcade.draw_line(0, 0, SCREEN_WIDTH/2, 0, arcade.color.BLUE, 5)
        arcade.draw_line(0, SCREEN_HEIGHT, SCREEN_WIDTH/2, SCREEN_HEIGHT, arcade.color.BLUE, 5)
        arcade.draw_line(0, 0, 0, SCREEN_HEIGHT, arcade.color.BLUE, 5)
        arcade.draw_line(SCREEN_WIDTH/2, 0, SCREEN_WIDTH, 0, arcade.color.RED, 5)
        arcade.draw_line(SCREEN_WIDTH/2, SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT, arcade.color.RED, 5)
        arcade.draw_line(SCREEN_WIDTH, 0, SCREEN_WIDTH, SCREEN_HEIGHT, arcade.color.RED, 5)
        arcade.draw_line(SCREEN_WIDTH/2, 0, SCREEN_WIDTH/2, SCREEN_HEIGHT, arcade.color.WHITE, 5)
        arcade.draw_circle_outline(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 100, arcade.color.WHITE, 5)
        self.ball.draw()
        self.player1.draw()
        self.player2.draw()
        arcade.draw_text('player1:'+ str(self.player1_score), (SCREEN_WIDTH/2-SCREEN_WIDTH/3), SCREEN_HEIGHT-50, color=arcade.color.BLUE_GRAY, font_size=15, bold=True,)
        arcade.draw_text('player2:'+ str(self.player2_score),(SCREEN_WIDTH/2+SCREEN_WIDTH/5), SCREEN_HEIGHT-50, color=arcade.color.RED_VIOLET, font_size=15, bold=True)
    def on_update(self, delta_time: float):
        self.ball.move()
        self.player1.move()
        self.player2.move()
        if self.check == 0:
            if self.player1_score == 5 or self.player2_score == 5: 
                if self.player1_score == 5:
                    winer = "player1"
                    self.check = 1
                else:
                    winer = "player2"
                    self.check = 1
                arcade.draw_rectangle_filled(0, 0, SCREEN_WIDTH*4, SCREEN_HEIGHT*4, arcade.color.MSU_GREEN)
                arcade.draw_text(f"{winer} win", SCREEN_WIDTH/2-150, SCREEN_HEIGHT/2, arcade.color.ALMOND, 50)
                arcade.finish_render()
        if self.ball.center_y < 40 or self.ball.center_y > SCREEN_HEIGHT - 40:
            self.ball.change_y *= -1
        
        if arcade.check_for_collision(self.player1, self.ball) or arcade.check_for_collision(self.player2, self.ball):
            self.ball.change_x *= -1

        if self.ball.center_x < 0:
            self.player2_score += 1
            del self.ball
            self.ball = Ball()

        if self.ball.center_x > SCREEN_WIDTH:
            self.player1_score += 1
            del self.ball
            self.ball = Ball()
        
    def on_key_press(self, key, modifiers: int):
        if key == arcade.key.UP:
            self.player1.change_y = 1
        elif key == arcade.key.DOWN:
            self.player1.change_y = -1
        elif key == arcade.key.W:
            self.player2.change_y = 1
        elif key == arcade.key.S:
            self.player2.change_y = -1

Game()
arcade.run()