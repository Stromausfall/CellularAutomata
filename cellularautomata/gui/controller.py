from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager


class Controller(BoxLayout):
    screen_manager = ObjectProperty()
    setup_screen_map_size = ObjectProperty()

    def finish_setup_settings_screen(self):
        sm:ScreenManager = self.screen_manager

        sm.current = "setup_map_screen"

        print("achange to setup_map_screen")

    def finish_setup_map_screen(self):
        sm:ScreenManager = self.screen_manager

        sm.current = "setup_settings_screen"

        print("achange to setup_settings_screen")

    def setup_settings_screen_map_size(self, value):
        return str(value) + "x" + str(value)