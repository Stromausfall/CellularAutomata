from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager


class Controller(BoxLayout):
    screen_manager = ObjectProperty()

    def foo_bar1(self):
        sm:ScreenManager = self.screen_manager

        sm.current = "screen_2"

        print("achange to screen_2")

    def foo_bar2(self):
        sm:ScreenManager = self.screen_manager

        sm.current = "screen_1"

        print("achange to screen_1")
