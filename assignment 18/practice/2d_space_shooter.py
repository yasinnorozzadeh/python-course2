import arcade
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700
SCREEN_TITLE = "2D space shooter"

class Heart(arcade.Sprite): 
    def __init__(self, x, y, color=":resources:images/items/gemGreen.png"):
        super().__init__(color)
        self.center_x = x
        self.center_y = y
        self.width = 80
        self.height = 80

class Bullet(arcade.Sprite):
    def __init__(self, x, y, a):
        super().__init__(":resources:images/space_shooter/laserBlue01.png")
        self.center_x = x
        self.center_y = y
        self.speed = 5
        self.angle = a
        self.change_x = 0
        self.change_y = 1

    def move(self):
        if self.angle == 90:
            self.center_y += self.speed
        elif self.angle == 270:
            self.center_y -= self.speed

class Spaceship(arcade.Sprite):
    def __init__(self, y, a, sprite=":resources:images/space_shooter/playerShip1_blue.png"):
        super().__init__(sprite)
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = y
        self.change_x = 0
        self.change_y = 0
        self.width = 50
        self.height = 50
        self.speed = 4
        self.angle = a
        self.Game_width = SCREEN_WIDTH
        self.Bullets = []
        self.heart = []

    def move(self):
        if self.change_x == -1:
            if self.center_x > 20:
                self.center_x += self.speed * self.change_x
        elif self.change_x == 1:
            if self.center_x < self.Game_width-20:
                self.center_x += self.speed * self.change_x

    def shoot(self, ang):
        new_bullet = Bullet(self.center_x, self.center_y, ang)
        if len(self.Bullets) <= 2: 
            self.Bullets.append(new_bullet)

    def hearts(self, y, c):
        x = 25
        for i in range(3):
            new_heart = Heart(x, y, c)
            self.heart.append(new_heart)
            x += 50

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.COOL_BLACK)
        self.player1 = Spaceship(SCREEN_HEIGHT-100, 180, ":resources:images/space_shooter/playerShip1_blue.png")
        self.player2 = Spaceship(100, 0, ":resources:images/space_shooter/playerShip1_green.png")
        self.player1.hearts(25, ":resources:images/items/gemGreen.png")
        self.player2.hearts(SCREEN_HEIGHT-25, ":resources:images/items/gemBlue.png")
        self.check = "start"

    def on_draw(self):
        arcade.start_render()
        if self.check == "game":
            self.player1.draw()
            self.player2.draw()
            for bullet in self.player1.Bullets:
                bullet.draw()
            for bullet in self.player2.Bullets:
                bullet.draw()
            for heart in self.player1.heart:
                heart.draw()
            for heart in self.player2.heart:
                heart.draw()

        elif self.check == "start":
            arcade.draw_text("W : player1 shoot", SCREEN_WIDTH/5, SCREEN_HEIGHT/3, font_size=15)
            arcade.draw_text("A : player1 move left", SCREEN_WIDTH/5, SCREEN_HEIGHT/3+20, font_size=15)
            arcade.draw_text("D : player1 move right", SCREEN_WIDTH/5, SCREEN_HEIGHT/3+40, font_size=15)
            arcade.draw_text("I : player2 shoot", SCREEN_WIDTH/5, SCREEN_HEIGHT/3+60, font_size=15)
            arcade.draw_text("L : player2 move right", SCREEN_WIDTH/5, SCREEN_HEIGHT/3+80, font_size=15)
            arcade.draw_text("J : player2 move left", SCREEN_WIDTH/5, SCREEN_HEIGHT/3+100, font_size=15)
            arcade.draw_text("Click a button to start game", SCREEN_WIDTH/2-200, SCREEN_HEIGHT/2+100, font_size=25)

        elif self.check == "w_1":
            arcade.draw_text("player green win", SCREEN_WIDTH/3, SCREEN_HEIGHT/2, font_size=15)

        elif self.check == "w_2":
            arcade.draw_text("player blue win", SCREEN_WIDTH/3, SCREEN_HEIGHT/2, font_size=15)

        arcade.finish_render()

    def on_key_release(self, synbol : int, modifiers: int):
        if synbol == arcade.key.A or synbol == arcade.key.D:
            self.player1.change_x = 0
        if synbol == arcade.key.J or synbol == arcade.key.L:
            self.player2.change_x = 0

    def on_key_press(self,synbol : int, modifiers: int):
        if self.check == "start":
            self.check = "game"
        elif self.check == "game":
            if synbol == arcade.key.A:
                self.player1.change_x = -1
            elif synbol == arcade.key.D:
                self.player1.change_x = 1
            elif synbol == arcade.key.W:
                self.player1.shoot(270)
                arcade.sound.play_sound(arcade.sound.load_sound(":resources:sounds/laser2.wav"))

            if synbol == arcade.key.J:
                self.player2.change_x = -1
            elif synbol == arcade.key.L:
                self.player2.change_x = 1
            elif synbol == arcade.key.I:
                self.player2.shoot(90)
                arcade.sound.play_sound(arcade.sound.load_sound(":resources:sounds/laser2.wav"))

    def on_update(self, delta_time):
        if self.check == "game":
            self.player1.move()
            self.player2.move()

            for bullet1 in self.player1.Bullets:
                bullet1.move()
            for bullet2 in self.player2.Bullets:
                bullet2.move()
            
            for bullet in self.player2.Bullets:
                if arcade.check_for_collision(self.player1, bullet):
                    
                    self.player2.Bullets.remove(bullet)
                    self.player2.heart.remove(self.player2.heart[0])
                if bullet.center_y > 600:
                    self.player1.Bullets.remove(bullet)
                if len(self.player1.heart) == 0:
                    arcade.sound.play_sound(arcade.sound.load_sound(":resources:sounds/explosion2.wav"))
                elif len(self.player2.heart) == 0:
                    arcade.sound.play_sound(arcade.sound.load_sound(":resources:sounds/explosion2.wav"))
            for bullet in self.player1.Bullets:
                if arcade.check_for_collision(self.player2, bullet):
                    self.player1.Bullets.remove(bullet)
                    self.player1.heart.remove(self.player1.heart[0])
                if bullet.center_y < 0:
                    self.player2.Bullets.remove(bullet)
                if len(self.player1.heart) == 0:
                    arcade.sound.play_sound(arcade.sound.load_sound(":resources:sounds/explosion2.wav"))
                elif len(self.player2.heart) == 0:
                    arcade.sound.play_sound(arcade.sound.load_sound(":resources:sounds/explosion2.wav"))
        if len(self.player1.heart) == 0:
            self.check = "w_2"
        elif len(self.player2.heart) == 0:
            self.check = "w_1"
Game()
arcade.run()