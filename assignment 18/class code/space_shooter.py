import arcade
from arcade.application import Window
WIDTH = 800
HEIGHT = 600
TITLE = "spase craft"
# First page
class  TitleView(arcade.View):

    def on_show(self):
        self.text = arcade.load_texture("")
        arcade.set_viewport()

    def on_draw(self):
        arcade.start_render()
        self.text.draw_sized()
    def on_key_press(self, key):
        if key == arcade.key.ENTER:
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)
            
# Final page

# Main view
class GameView(arcade.View):
    def __init__():
        pass

    def setup(self):
        pass

    def on_draw(self):
        pass

    def on_key_press(self):
        pass

    def update(self):
        pass


def main():
    window = arcade.Window(WIDTH, HEIGHT, TITLE)
    start = TitleView()
    window.show_view(start)
    arcade.run()
if __name__ == "__main__":
    main()