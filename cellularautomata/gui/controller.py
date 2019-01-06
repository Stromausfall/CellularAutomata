from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager

from cellularautomata.gui.setupmap.clickabletile import ClickableTile
from cellularautomata.gui.setupmap.unclickabletile import UnclickableTile


class Controller(BoxLayout):
    setup_screen_map_size = ObjectProperty()

    def finish_setup_settings_screen(self, screen_manager: ScreenManager, container: GridLayout):
        screen_manager.current = "setup_map_screen"

        # file the setup map screen with buttons
        for row in range(container.rows):
            for column in range(container.cols):
                button: Button = ClickableTile(row=row, column=column)

                container.add_widget(button)

    def finish_setup_map_screen(self, setup_map_screen_content: GridLayout, simulation_screen_content: GridLayout,
                                screen_manager: ScreenManager):
        for tile in sorted(setup_map_screen_content.children):
            clickableTile: ClickableTile = tile
            unclickableTile: UnclickableTile = UnclickableTile(row=clickableTile.row, column=clickableTile.column,
                                                               is_alive=clickableTile.is_selected)

            simulation_screen_content.add_widget(unclickableTile)

        screen_manager.current = "simulation_screen"

    def setup_settings_screen_map_size_text(self, map_size: int):
        return str(map_size) + "x" + str(map_size)

    def simulation_screen_speed_text(self, speed: int):
        return "%.1f gen/s" % (speed)
