from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.layout import Layout
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.widget import Widget

from cellularautomata.gui.gui import Gui
from cellularautomata.gui.screens.setup.controller import Controller


class TestApp(App):

    def build_grid(self):
        count = 10

        layout: Layout = GridLayout(cols=count)

        for x in range(count):
            for y in range(count):
                label_text = '[' + str(x) + ' / ' + str(y) + ']'
                label: Label = Label(text=label_text)
                layout.add_widget(label)

        # return button
        return layout

    def build(self):
        return Controller()

    # def build(self):
    #     button: Widget = Button(text='Hello World')
    #     grid: Layout = self.build_grid()
    #
    #     layout: Layout = BoxLayout(orientation='vertical')
    #
    #     content_1: Layout = BoxLayout(size_hint=(1, .7))
    #     content_2: Layout = BoxLayout(size_hint=(1, .3))
    #
    #     content_1.add_widget(button)
    #     content_2.add_widget(grid)
    #
    #     layout.add_widget(content_1)
    #     layout.add_widget(content_2)
    #
    #
    #     #return layout
    #     #sm = ScreenManager()
    #     #Gui(screen_manager=sm)
    #     #return sm
    #
    #     #return Gui()
    #     return Builder.load_fil


TestApp().run()
