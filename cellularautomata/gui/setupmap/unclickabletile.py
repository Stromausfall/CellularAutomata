from kivy.properties import BooleanProperty
from kivy.uix.button import Button


class UnclickableTile(Button):
    is_alive = BooleanProperty(False)

    def on_is_alive(self, instance, value):
        if value:
            self.background_color = self.__selected_color
        else:
            self.background_color = self.__not_selected_color

    def on_touch_down( self, touch ):
        pass

    def __init__(self, row: int, column: int, is_alive: bool):
        Button.__init__(self)

        self.__not_selected_color = self.background_color
        self.__selected_color = [0.0, 1.0, 1.0, 1.0]

        self.row = row
        self.column = column
        self.is_alive = is_alive
