import random
import arcade 
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
class Apple(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.image = "apple.jpg"
        self.apple = arcade.Sprite(self.image, 0.04)
        self.apple.center_x = random.randint(20 ,w - 20)
        self.apple.center_y = random.randint(20 ,h - 20)
    def draw(self):
        self.apple.draw()

class Pear:
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.image = "pear.jpg"
        self.pear = arcade.Sprite(self.image, 0.2)
        self.pear.center_x = random.randint(20, w - 20)
        self.pear.center_y = random.randint(20, h - 20)
    def draw(self):
        self.pear.draw()

class Poop:
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.image = "poop.jpg"
        self.poop = arcade.Sprite(self.image, 0.1)
        self.poop.center_x = random.randint(20, w -20)
        self.poop.center_y = random.randint(20, h -20)
    def draw(self):
        self.poop.draw()

class Snake(arcade.Sprite):
    def __init__(self , w , h):
        arcade.Sprite.__init__(self)
        self.speed = 3
        self.width = 20
        self.height = 20
        self.r = 10
        self.snake_score = 1
        self.center_x = w // 2
        self.center_y = h // 2
        self.change_x = 0
        self.change_y = 0
        self.body_colors = [arcade.color.AMAZON, arcade.color.ANDROID_GREEN, arcade.color.AO, arcade.color.AVOCADO, arcade.color.BANGLADESH_GREEN, arcade.color.BRIGHT_GREEN, arcade.color.BITTER_LEMON, arcade.color.DARK_OLIVE_GREEN]
        self.body = []
        self.length = 0

    def draw(self):
        self.body.append([self.center_x, self.center_y])
        for body_item in self.body:
            if body_item == [self.center_x, self.center_y]:
                arcade.draw_circle_filled(body_item[0], body_item[1], self.r+3, arcade.color.CHARLESTON_GREEN)
            else:
                arcade.draw_circle_filled(body_item[0], body_item[1], self.r ,random.choice(self.body_colors))
            if len(self.body) > self.length:
                self.body.pop(0)

    def move(self):
        if self.speed <= 10:
            self.center_x += self.speed * self.change_x
            self.center_y += self.speed * self.change_y
        else:
            self.center_x += 10 * self.change_x
            self.center_y += 10 * self.change_y

    def game_over(self):
        arcade.draw_text('GAME OVER', SCREEN_WIDTH//2, SCREEN_HEIGHT//2, arcade.color.BLACK, 5 * 5, width=SCREEN_WIDTH, align='left')
        arcade.exit()

    def score_food(self, snake_food):
        if snake_food == "apple":
            self.snake_score += 1
            self.length += 2
            self.speed += 0.05
        elif snake_food == "pear":
            self.snake_score += 2
            self.length += 3
            self.speed += 0.5
        elif snake_food == "poop":
            self.snake_score -= 1
            if self.snake_score == 0:
                self.game_over()
            else:
                self.speed -= 1
                self.body.pop()

class Game(arcade.Window):
    def __init__(self):
        arcade.Window.__init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, "Snake_game")
        arcade.set_background_color(arcade.color.SAND)
        self.apple = Apple(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.pear = Pear(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.poop = Poop(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.snake = Snake(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.heighest_score = 0
        self.score = f"Score: {self.snake.snake_score}"
        self.heigh_score = f"Heighest Score: {self.heighest_score}"
    
    def on_draw(self):
        arcade.start_render()
        self.apple.draw()
        self.pear.draw()
        self.poop.draw()
        self.snake.draw()
        arcade.draw_line(0, 0, 700, 0, arcade.color.WARM_BLACK, 20)
        arcade.draw_line(0, 0, 0, 700, arcade.color.WARM_BLACK, 20)
        arcade.draw_line(700, 700, 0, 700, arcade.color.WARM_BLACK, 20)
        arcade.draw_line(700, 700, 700, 0, arcade.color.WARM_BLACK, 20)
        arcade.draw_text(self.score, 10, SCREEN_HEIGHT-30, arcade.color.GRAPE, 15)
        arcade.draw_text(self.heigh_score, 10, SCREEN_HEIGHT-50, arcade.color.GRAPE, 15)
        

    def on_update(self, delta_time: float):
        self.snake.move()
        if arcade.check_for_collision(self.snake, self.apple.apple):
            self.snake.score_food("apple")
            self.apple = Apple(SCREEN_WIDTH, SCREEN_HEIGHT)
        elif arcade.check_for_collision(self.snake, self.pear.pear):
            self.snake.score_food("pear")
            self.pear = Pear(SCREEN_WIDTH, SCREEN_HEIGHT)
        elif arcade.check_for_collision(self.snake, self.poop.poop):
            self.snake.score_food("poop")
            self.poop = Poop(SCREEN_WIDTH, SCREEN_HEIGHT)
        if self.snake.center_x <= 20 or self.snake.center_x >= SCREEN_WIDTH-20 or self.snake.center_y <= 20 or self.snake.center_y >= SCREEN_HEIGHT-20:
            self.snake.game_over()
            

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP  or key == arcade.key.W:
            self.snake.change_x = 0
            self.snake.change_y = 1
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.snake.change_x = 0
            self.snake.change_y = -1
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.snake.change_x = -1
            self.snake.change_y = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.snake.change_x = 1
            self.snake.change_y = 0


Game()
arcade.run()
