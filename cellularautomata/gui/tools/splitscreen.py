from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.layout import Layout


class SplitScreen(BoxLayout):
    def __init__(self, top_ratio: float):
        BoxLayout.__init__(self, orientation='vertical')

        # create the two child containers (define how large they should be)
        self.top_screen_half: Layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint=(1, top_ratio))
        self.bottom_screen_half: Layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint=(1, 1 - top_ratio))

        # add them to the parent container
        self.add_widget(self.top_screen_half)
        self.add_widget(self.bottom_screen_half)
