import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Drawing With Loops Example"


def draw_background():
    arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT * 2 / 3, SCREEN_WIDTH - 1, SCREEN_HEIGHT * 2 / 3, arcade.color.SKY_BLUE)
    arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 6, SCREEN_WIDTH - 1, SCREEN_HEIGHT / 3, arcade.color.DARK_SPRING_GREEN)

def draw_bird(x, y):
    arcade.draw_arc_outline(x, y, 40, 40, arcade.color.BLACK, 0, 90)
    arcade.draw_arc_outline(x + 40, y, 40, 40, arcade.color.BLACK, 90, 180)

def draw_pine_tree(center_x, center_y):
    arcade.draw_rectangle_filled(center_x, center_y, 20, 40, arcade.color.DARK_BROWN)
    tree_bottom_y = center_y + 20
    point_list = ((center_x - 40, tree_bottom_y), (center_x, tree_bottom_y + 100), (center_x + 40, tree_bottom_y))
    arcade.draw_polygon_filled(point_list, arcade.color.DARK_GREEN)
def draw_cloud(x, y, c):
    arcade.draw_circle_filled(x + 70, y + 20 , 100, c, num_segments=-1)
    arcade.draw_circle_filled(x + 160, y-10, 70, c, num_segments=-1)
    arcade.draw_circle_filled(x + 160, y + 40, 70, c, num_segments=-1)
    arcade.draw_circle_filled(x , y-10, 70, c, num_segments=-1)
    arcade.draw_circle_filled(x, y + 40, 70, c, num_segments=-1)
def draw_sun():
    arcade.draw_circle_filled(500, 550, 40, arcade.color.YELLOW)
  
    # Rays to the left, right, up, and down
    arcade.draw_line(500, 550, 400, 550, arcade.color.YELLOW, 3)
    arcade.draw_line(500, 550, 600, 550, arcade.color.YELLOW, 3)
    arcade.draw_line(500, 550, 500, 450, arcade.color.YELLOW, 3)
    arcade.draw_line(500, 550, 500, 650, arcade.color.YELLOW, 3)
    
    # Diagonal ray
    arcade.draw_line(500, 550, 550, 600, arcade.color.YELLOW, 3)
    arcade.draw_line(500, 550, 550, 500, arcade.color.YELLOW, 3)
    arcade.draw_line(500, 550, 450, 600, arcade.color.YELLOW, 3)
    arcade.draw_line(500, 550, 450, 500, arcade.color.YELLOW, 3)

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.start_render()
draw_background()
draw_cloud(0, 450, arcade.color.CELESTE)
draw_cloud(150, 550, arcade.color.BRIGHT_CERULEAN)
draw_cloud(350, 450, arcade.color.AQUAMARINE)
draw_cloud(550, 500, arcade.color.BALL_BLUE)
draw_sun()
for bird_count in range(10):
    x = random.randrange(0, SCREEN_WIDTH)
    y = random.randrange(SCREEN_HEIGHT // 3, SCREEN_HEIGHT - 20)
    draw_bird(x, y)

for x in range(80, SCREEN_WIDTH-80, 100):
    draw_pine_tree(random.randrange(x - 45, SCREEN_WIDTH-45), random.randrange(SCREEN_HEIGHT / 5))

arcade.finish_render()
arcade.run()
