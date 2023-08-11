import arcade
WIDTH = 600
HEIGHT = 600
TITLE = "imoji picture"
arcade.open_window(WIDTH, HEIGHT, TITLE)
arcade.set_background_color(arcade.color.PERSIMMON)
arcade.start_render()
arcade.draw_circle_filled(300, 300, 250, arcade.color.YELLOW_ROSE)
texture = arcade.load_texture("پروژه_ی جدید.png")
arcade.draw_lrwh_rectangle_textured(50, 280, 500, 150,  texture)
# arcade.draw_arc_outline(300, 210, 120, 100, arcade.color.BLACK, 190, 350, 100)
arcade.draw_lrwh_rectangle_textured(-510, -300, 1800, 900, arcade.load_texture("smile.png"))
arcade.finish_render()
arcade.run()