from kivy.properties import BooleanProperty
from kivy.uix.button import Button


class ClickableTile(Button):
    is_selected = BooleanProperty(False)

    def on_is_selected(self, instance, value):
        if value:
            self.background_color = self.__selected_color
        else:
            self.background_color = self.__not_selected_color

    def setup_map_screen_tile_clicked(self, tile: Button):
        self.is_selected = not self.is_selected

    def __init__(self, row: int, column: int):
        Button.__init__(self, on_press=self.setup_map_screen_tile_clicked)

        self.row = row
        self.column = column
        self.is_selected = False

        self.__not_selected_color = self.background_color
        self.__selected_color = [0.0, 1.0, 1.0, 1.0]

    # creates an ordering of ClickableTiles (first row, then column)
    def __lt__(self, other):

        if self.row == other.row:
            return self.column < other.column
        else:
            return self.row < other.row
