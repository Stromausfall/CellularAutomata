from kivy.uix.screenmanager import ScreenManager

from cellularautomata.gui.screens.setup.setupscreen import SetupScreen


class Gui(ScreenManager):

    def __init__(self):
        ScreenManager.__init__(self)

        self.add_widget(SetupScreen())
