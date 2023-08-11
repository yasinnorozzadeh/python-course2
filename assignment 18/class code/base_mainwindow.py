import arcade

WIDTH = 400
HEIGHT = 400

class Mygame(arcade.Window):
    def __init__(self, w, h):
        super().__init__(w, h)
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self): pass
    def on_draw(self):
        arcade.start_render()
    # def update(self): pass

def main():
    game = Mygame(WIDTH, HEIGHT)
    game.setup()
    arcade.run()
if __name__ == "__main__":
    main()