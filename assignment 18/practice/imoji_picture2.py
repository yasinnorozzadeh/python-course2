import arcade
WIDTH = 600
HEIGHT = 600
TITLE = "imoji picture"
arcade.open_window(WIDTH, HEIGHT, TITLE)
arcade.set_background_color(arcade.color.PERSIMMON)
arcade.start_render()
arcade.draw_circle_filled(300, 300, 250, arcade.color.YELLOW_ROSE)
arcade.draw_circle_filled(150, 250, 30, arcade.color.PINK_LAVENDER)
arcade.draw_circle_filled(450, 250, 30, arcade.color.PINK_LAVENDER)
arcade.draw_arc_outline(200, 400, 100, 85, arcade.color.BLACK, 190, 360 , 30)
arcade.draw_arc_outline(400, 400, 100, 85, arcade.color.BLACK, 190, 360 , 30)
arcade.draw_arc_outline(300, 200, 200, 150, arcade.color.BLACK,190, 350, 10)
arcade.draw_triangle_filled(300, 50, 200, 100, 200, 0, arcade.color.FALU_RED)
arcade.draw_triangle_filled(300, 50, 400, 100, 400, 0, arcade.color.FALU_RED)
arcade.finish_render()
arcade.run()