from kivy.app import App

from cellularautomata.gui.controller import Controller


class CellularAutomataApp(App):

    def build(self):
        return Controller()


CellularAutomataApp().run()
