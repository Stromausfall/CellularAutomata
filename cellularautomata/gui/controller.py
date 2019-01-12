import numpy
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager

from cellularautomata.gui.setupmap.clickabletile import ClickableTile
from cellularautomata.gui.setupmap.unclickabletile import UnclickableTile
from cellularautomata.logic.calculationinteraction import CalculationInteraction


class Controller(BoxLayout):
    simulation_screen_content = ObjectProperty()

    def __init__(self):
        BoxLayout.__init__(self)
        self.__calculation_thread_interaction:CalculationInteraction = None

    def finish_setup_settings_screen(self, screen_manager: ScreenManager, container: GridLayout):
        screen_manager.current = "setup_map_screen"

        # fill the setup map screen with buttons
        for row in range(container.rows):
            for column in range(container.cols):
                button: Button = ClickableTile(row=row, column=column)

                container.add_widget(button)

    def get_ndarray_from(self, grid_layout: GridLayout) -> numpy.ndarray:
        biggest_tile: ClickableTile = sorted(grid_layout.children)[-1]

        result: numpy.ndarray = numpy.empty(shape=(biggest_tile.row+1, biggest_tile.column+1))
        for tile in grid_layout.children:
            result[tile.row][tile.column] = tile.is_selected

        return result

    def finish_setup_map_screen(self, screen_manager: ScreenManager, setup_map_screen_content: GridLayout):
        # create unclickable tiles and add them to the screen
        for tile in sorted(setup_map_screen_content.children):
            clickableTile: ClickableTile = tile
            unclickableTile: UnclickableTile = UnclickableTile(row=clickableTile.row, column=clickableTile.column,
                                                               is_alive=clickableTile.is_selected)

            self.simulation_screen_content.add_widget(unclickableTile)

        # switch screen
        screen_manager.current = "simulation_screen"

        # create the CalculationThreadInteraction instance
        self.__calculation_thread_interaction = CalculationInteraction(
            self.get_ndarray_from(setup_map_screen_content))

        # start calling the callback every frame
        Clock.schedule_interval(self.display_newest_world, 0)

    def display_newest_world(self, *largs):
        newest_world:numpy.ndarray = self.__calculation_thread_interaction.get_newest_world()

        for tile in self.simulation_screen_content.children:
            tile.is_alive = newest_world[tile.row][tile.column]

    def simulation_speed_slider_value_change(self, value:float):
        self.__calculation_thread_interaction.change_generations_per_second(value)

    def setup_settings_screen_map_size_text(self, map_size: int):
        return str(map_size) + "x" + str(map_size)

    def simulation_screen_speed_text(self, speed: int):
        return "%.1f gen/s" % (speed)
