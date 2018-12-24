from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.slider import Slider

from cellularautomata.gui.tools.splitscreen import SplitScreen


class SetupScreen(Screen):

    def __init__(self):
        Screen.__init__(self, name="Setup screen")

        # create a split screen container
        self.__split_screen = SplitScreen(0.75)

        # add the container to the screen
        self.add_widget(self.__split_screen)

        layout: AnchorLayout = AnchorLayout(anchor_x='center', anchor_y='center')

        # add controls to change the map size
        self.__add_map_size()

    def _map_size_event(self, instance, value):
        self.__map_size_label.text = str(value) + "x" + str(value)

    def __add_map_size(self):
        # create the container for the content (and add it to the top screen half)
        box_layout: BoxLayout = BoxLayout(orientation='vertical')
        self.__split_screen.top_screen_half.add_widget(box_layout)

        # create the slider and bind a method to capture value changes
        slider: Slider = Slider(min=10, max=40, value=25, step=1)
        slider.bind(value=self._map_size_event)

        # compose the parts
        self.__map_size_label: Label = Label()
        box_layout.add_widget(Label(text="Size of cellular automata"))
        box_layout.add_widget(slider)
        box_layout.add_widget(self.__map_size_label)

        # change the slider.value -> this causes an automatic redrawing of the label!
        slider.value = slider.min
